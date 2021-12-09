import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
from decimal import Decimal
import networkit as nk

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

#PLOTTA SCATTER PLOT
plt.yscale('log')
plt.xscale('log')
f = plt.figure(num=1)
f.set_figheight(8)
f.set_figwidth(10)
plt.xticks(fontsize=12,weight='bold')
plt.yticks(fontsize=12,weight='bold')
plt.ylabel('EARNED TOKEN', fontsize=18,weight='bold')
plt.xlabel('NODE DEGREE',fontsize=18,weight='bold')
plt.title('RELATION BETWEEN NODE DEGREE AND EARNED TOKEN',fontsize=20,weight='bold')
plt.scatter(dfg_tot['degree'],dfg_tot['in_token'])
plt.savefig('./risultati_analisi/scatter_norum/scatter'+n+'_norum.png')
