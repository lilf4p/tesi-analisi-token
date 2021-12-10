#GRAFICO CON MEDIA E VARIANZA
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from decimal import Decimal
import networkit as nk

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

n = '1'
weight = 'val_sum'

fname = './trx_contract/trx_contract_riprova_'+str(n)+'.csv'
edgelist = "./edgelist/edgelist_"+str(n)+".csv"

#CALCOLA TOKEN RICEVUTI PER OGNI NODO 
df = pd.read_csv(fname)
df[weight] = ['%E' % Decimal(v) for v in df[weight]]
df[weight]=df[weight].astype('float64')
print(df)
print(df.dtypes)
dfg = df.groupby(['to_address'])[weight].sum().reset_index(name='in_token')
print(dfg)
print(dfg.dtypes)

#CALCOLA IL GRADO DI OGNI NODO
reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
g = reader.read(edgelist)
gu = nk.graphtools.toUndirected(g)
dd = nk.centrality.DegreeCentrality(gu).run()
list_res = sorted(dd.ranking())
print(list_res[:10])

#UNISCI 
l = list(df['from_address'])+(list(df['to_address']))
list_nodes = sorted(list(dict.fromkeys(l)))
print(list_nodes[:10])
dict_token = dict()
for u in list_nodes:
    dict_token[u] = 0

token = dict (zip(dfg['to_address'],dfg['in_token']))
for k,v in token.items():
    dict_token[k] = dict_token[k] + v
#print(dict_token)
dfg_tot = pd.DataFrame(list(dict_token.items()),columns=['id','in_token'])
id_nodi,gradi = zip(*list_res)
dfg_tot['degree'] = gradi
print (dfg_tot)

#ELIMINA NODI CON 0 TOKEN GUADAGNATI
dfg_tot = dfg_tot[dfg_tot.in_token != 0].reset_index()
print(dfg_tot)

#GROUPBY DEGREE -> OTTIENI GLI ARRAY TOKEN_i
dflist = dfg_tot.groupby('degree')['in_token'].apply(list).reset_index(name='in_token_list')
print(dflist)

#PER OGNI IN_TOKEN_LIST CALCOLA MEDIA E DEVIAZIONE STD
list_mean = []
list_dev = []
list_len = []
lt = dflist['in_token_list'].tolist()
print('numero liste :'+str(len(lt)))
for l in lt:
    list_len.append(len(l)) #LUNGHEZZE ARRAY TOKEN
    arr = np.array(l)
    mean = arr.mean() #MEDIA
    list_mean.append(mean)
    dev = arr.std() #DEVIAZIONE STD
    list_dev.append(dev)

print(list_dev)
print(list_mean)
print(list_len)
#PLOTTA SCATTER PLOT
plt.yscale('log')
plt.xscale('log')
f = plt.figure(num=1)
f.set_figheight(9)
f.set_figwidth(12)
plt.xticks(fontsize=12,weight='bold')
plt.yticks(fontsize=12,weight='bold')
plt.ylabel('EARNED TOKEN', fontsize=16,weight='bold')
plt.xlabel('NODE DEGREE',fontsize=16,weight='bold')
#plt.errorbar(dflist['degree'],list_mean,yerr=list_dev,fmt='none',lw=1,capsize=3)
scat = plt.scatter(dflist['degree'],list_mean,c=list_dev,s=list_len,alpha=0.3)
cb = f.colorbar(scat)
cb.set_label("STANDARD DEVIATION", size='x-large',weight='bold')
cb.ax.tick_params(labelsize=12)
plt.title(cname[int(n)]+'\n RELATION BETWEEN NODE DEGREE AND EARNED TOKEN',fontsize=18,weight='bold')
plt.savefig('./risultati_analisi/scatter_var/scatter'+n+'_var.png',format='png')
