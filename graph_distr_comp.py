import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import networkit as nk
import pandas as pd
from sklearn.preprocessing import MinMaxScaler 
from sklearn.preprocessing import RobustScaler 
import seaborn as sns
import numpy as np

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

list_patch = []
ldf = []
z=0
ax = None
#labels = []
#ndf = pd.DataFrame(columns=['contratto','1','2','3','4','other'])
for color,n in zip(mcolors.TABLEAU_COLORS,range(1,11)):
    fname = "./edgelist/edgelist_"+str(n)+".csv"
    reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
    print(fname+" letto")
    try:
        g = reader.read(fname)
    except: 
        print("File not exist")
        exit()

    wc = nk.components.WeaklyConnectedComponents(g).run() 
    dict_comp = wc.getComponentSizes() #Returns a map with the component indexes as keys, and their size as values
    
    #GROUPBY SIZE
    df = pd.DataFrame(list(dict_comp.items()),columns=['id_comp','size'])
    dfg = df.groupby(['size']).size().reset_index(name='counts')

    #SULLE Y VORREI (NUMERO DI COMPONENTI/COMP TOT)*100
    #NORMALIZZARE
    #nc = wc.numberOfComponents()
    #list_occ_norm = [((int(occ)/nc)*100) for occ in list_occ]
    #list_size_ord = sorted(list_size)
    #max_size = list_size_ord[-1]
    #list_size_norm = [((int(sz)/max_size)*100) for sz in list_size_ord]

    #NORMALIZZO MIN-MAX
    #dfg = dfg.iloc[1: , :]
    #scaler = MinMaxScaler()
    #dfg = pd.DataFrame(scaler.fit_transform(dfg),columns=['size','counts'])
    #print(dfg)
    
    #NORMAILIZZO  
    #scaler = RobustScaler()
    #dfg = pd.DataFrame(scaler.fit_transform(dfg),columns=dfg.columns)
    dfg['size'] = (dfg['size'] - dfg['size'].min()) / (dfg['size'].max() - dfg['size'].min())

    print(dfg)
    #CALCOLO CDF
    #pdf
    dfg['pdf'] = dfg['counts'] / sum(dfg['counts'])
    #print(dfg)
    #cdf
    dfg['cdf'] = dfg['pdf'].cumsum()
    dfg = dfg.reset_index()
    print(dfg)
    ax = dfg.plot(x = 'size', y = 'cdf', grid = True, ax=ax, marker='.')

    #RECUPERO LE DUE LISTE DA PLOTTARE 
    #list_occ_norm = dfg_norm[1].tolist()
    #list_size_norm = dfg_norm[0].tolist()
    
    #plotto 
    #ax = dfg_norm.plot(x='size',y='counts',kind='line',ax=ax)
    
    #BOXPLOT
    #ldf.append(dfg.assign(Location=cname[n]))
    
    #SCRIVI NOME CONTRATTO AL POSTO DEL NUMERO
    patch = mpatches.Patch(color=color, label=cname[n])
    list_patch.append(patch)

#plt.xscale("symlog")
#plt.yscale("symlog")
#cdf = pd.concat(ldf)
#print (cdf)
#ax = sns.boxplot(x="Location", y="size", data=cdf)
plt.xticks(fontsize=12,weight='bold')
plt.yticks(fontsize=12,weight='bold')
plt.ylabel('FREQUENCY', fontsize=18,weight='bold')
plt.xlabel('SIZE OF COMPONENT (noramlized)',fontsize=18,weight='bold')
plt.title('COMPONENT SIZE DISTRIBUTION',fontsize=20,weight='bold')
plt.legend(handles=list_patch,fontsize=15)    
f = plt.figure(num=1)
f.set_figheight(10)
f.set_figwidth(10)
plt.savefig('./risultati_analisi/cdf_size_comp_norm.png')
#print(wc.numberOfComponents())
#plt.savefig('./risultati_analisi/istog_comp_conn.png')