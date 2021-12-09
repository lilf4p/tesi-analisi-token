from numpy import longlong
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
from operator import itemgetter
import numpy as np
from decimal import Decimal
from sklearn.preprocessing import MinMaxScaler 
import seaborn as sns


cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

weights = ['val_avg','val_min','val_max','val_sum'] #CAMBIA PER CALCOLARE LA DISTRIBUZIONE DI WEIGHT DIVERSI  

weight = 'val_avg'   
ldf=[]
for color,n in zip(mcolors.TABLEAU_COLORS,range(1,11)):
    fname = './trx_contract/trx_contract_'+str(n)+'.csv'
    #CREO DATAFRAME E CONVERTO IN NUMERI RAPPRESENTABILI
    df = pd.read_csv(fname)
    df[weight] = ['%E' % Decimal(v) for v in df[weight]]
    df[weight]=df[weight].astype('float64')
    print(df)
    print(df.dtypes)
    #CALCOLO LE OCCORRENZE    
    dfg = df.groupby([weight]).size().reset_index(name='counts')
    print(dfg)
    print(dfg.dtypes)
    
    #NORMALIZZO MINMAX LA MISURA WEIGHT
    scaler = MinMaxScaler()
    dfg_norm = pd.DataFrame(scaler.fit_transform(dfg),columns=[weight,'counts'])
    #dfg[weight] = (dfg[weight] - dfg[weight].min()) / (dfg[weight].max() - dfg[weight].min())
    #print(dfg_norm)
    #CALCOLO LE FREQUENZE NORMALIZZATE CON CDF
    #pdf
    #dfg['pdf'] = dfg['counts'] / sum(dfg['counts'])
    #cdf
    #dfg['cdf'] = dfg['pdf'].cumsum()
    #dfg = dfg.reset_index()
    #print(dfg)
    #NORMALIZZA OCCORRENZE
    #nv = len(df.index)
    #dfg['counts'] = [((occ/nv)*100) for occ in dfg['counts']]
    #print(dfg)
    #TRASLO LE MISURE SULL'ASSE X DI UNO A DESTRA PER POTER RAPPRESENTARE LO 0 IN LOGSCALE (0 -> 1)
    #dfg[weight] = dfg[weight] + np.float64('%E' % Decimal('1'))
    #print(dfg)
    #PLOTTO IL DATAFRAME ELABORATO
    #ax = dfg.plot (x=weight,y='cdf',ax=ax)
    #BOXPLOT
    ldf.append(dfg_norm.assign(Location=cname[n]))
#plt.xscale('log')
#plt.yscale('log')
plt.ylim(top=0.001)
cdf = pd.concat(ldf)
print (cdf)
f = plt.figure(num=1)
sns.boxplot(x="Location", y=weight, data=cdf)
f.set_figheight(10)
f.set_figwidth(10)
plt.xticks(fontsize=12,weight='bold')
plt.yticks(fontsize=12,weight='bold')
#plt.legend(fontsize=15,handles=list_patch)    
#CAMBIA IN BASE A WEIGHT
if weight == 'val_avg':
    s = 'AVARAGE'
elif weight == 'val_min':
    s = 'MIN'
elif weight == 'val_max':
    s = 'MAX'
elif weight == 'val_sum':
    s = 'SUM'

plt.ylabel(s+' TOKEN TRANSFER (zoom)', fontsize=18,weight='bold')
plt.xlabel('CONTRACTS',fontsize=18,weight='bold') 
plt.title(s+' TOKEN TRANSFER DISTRUBUTION',fontsize=18,weight='bold')
plt.savefig('./risultati_analisi/boxplot_val_zoom/boxplot_'+weight+'_zoom.png')
