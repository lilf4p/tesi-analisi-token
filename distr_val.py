import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}
list_patch = []
ax = None


for color,n in zip(mcolors.TABLEAU_COLORS,range(1,11)):    
    fname = './trx_contract/trx_contract_'+str(n)+'.csv'
    df = pd.read_csv(fname)
    print(df)
    dfg = df.groupby(['val_avg']).size().reset_index(name='counts')
    #print(dfg['val_max'].tolist())
    #print(dfg.dtypes)
    #dfg.astype('int64')
    #print(dfg.dtypes)
    #dfg['val_avg'] = dfg['val_avg'] + 1
    print(dfg)
    #print(dfg['counts'].tolist())
    ax = dfg.plot (x='val_avg',ax=ax, marker='.')
    #plt.plot(dfg['val_max'].tolist(), dfg['counts'].tolist())
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
plt.xlabel('AVERAGE TOKEN TRANSFER',fontsize=18,weight='bold')
plt.title('NODES DEGREE DISTRIBUTION',fontsize=18,weight='bold')
plt.legend(fontsize=15,handles=list_patch)    
plt.savefig('./risultati_analisi/distr_avgtoken.png')