from numpy import longlong
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
from operator import itemgetter
import numpy as np
from decimal import Decimal

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}
list_patch = []
ax = None

weight = 'val_avg' #CAMBIA PER CALCOLARE LA DISTRIBUZIONE DI WEIGHT DIVERSI  

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
    #scaler = MinMaxScaler()
    #dfg = pd.DataFrame(scaler.fit_transform(dfg),columns=['degree','counts'])
    #dfg[weight] = (dfg[weight] - dfg[weight].min()) / (dfg[weight].max() - dfg[weight].min())
    #print(dfg)

    #CALCOLO LE FREQUENZE NORMALIZZATE CON CDF
    #pdf
    dfg['pdf'] = dfg['counts'] / sum(dfg['counts'])
    #cdf
    dfg['cdf'] = dfg['pdf'].cumsum()
    dfg = dfg.reset_index()

    #TRASLO LE MISURE SULL'ASSE X DI UNO A DESTRA PER POTER RAPPRESENTARE LO 0 IN LOGSCALE (0 -> 1)
    dfg[weight] = dfg[weight] + np.float64('%E' % Decimal('1'))
    print(dfg)

    #PLOTTO IL DATAFRAME ELABORATO
    ax = dfg.plot (x=weight,y='counts',ax=ax, marker='.')

    patch = mpatches.Patch(color=color, label=cname[n])
    list_patch.append(patch)

plt.xscale('log')
plt.yscale('log')
f = plt.figure(num=1)
f.set_figheight(10)
f.set_figwidth(10)
plt.xticks(fontsize=12,weight='bold')
plt.yticks(fontsize=12,weight='bold')
plt.ylabel('FREQUENCY', fontsize=18,weight='bold')
plt.legend(fontsize=15,handles=list_patch)    

#CAMBIA IN BASE A WEIGHT
plt.xlabel('AVERAGE TOKEN TRANSFER',fontsize=18,weight='bold') 
plt.title('AVERAGE TOKEN TRANSFER DISTRUBUTION',fontsize=18,weight='bold')
plt.savefig('./risultati_analisi/distr_avgtoken.png')

