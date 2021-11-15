import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import networkit as nk
import matplotlib.ticker as mtick
import pandas as pd
import csv
from pandas.io.formats import style
from sklearn.preprocessing import MinMaxScaler 
import seaborn as sns

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

fo = open('./risultati_analisi/media_var_degree.csv','w')
csv_writer = csv.writer(fo)
csv_writer.writerow(['contratto','media','varianza'])

list_patch = []
ax = None
#bdf = pd.DataFrame(columns=['USDT','MGC','LINK','WETH','EOS','BAT','OMG','CPCT','TRX','SHIB'])
ldf = []
for color,n in zip(mcolors.TABLEAU_COLORS,range(1,11)):

    fname = "./edgelist/edgelist_"+str(n)+".csv"
    reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
    try:
        g = reader.read(fname)
    except: 
        print("File not exist")
        exit()
    gu = nk.graphtools.toUndirected(g)
    dd = nk.centrality.DegreeCentrality(gu).run()
    list_res = dd.ranking()
 
    #GROUPBY(VALORE) -> OCCORRENZE DI OGNI VALORE
    df = pd.DataFrame(list_res,columns=['id_node','degree'])
    dfg = df.groupby(['degree']).size().reset_index(name='counts')

    #media
    #media = df['degree'].mean()
    #var = df['degree'].var()
    #csv_writer.writerow([n,media,var])

    #NORMALIZZARE - MAX
    #nt = gu.numberOfNodes()
    #list_occ_norm = [((int(occ)/nt)*100) for occ in list_occ]

    #list_gradi_sorted = sorted(list_gradi)
    #max_degree = list_gradi_sorted[-1]
    ##print(max_degree)
    #list_gradi_norm = [((int(gradi)/int(max_degree))*100) for gradi in list_gradi_sorted]

    #NORMALIZZO - MINMAX
    print(dfg)
    #dfg = dfg.iloc[1: , :]
    #scaler = MinMaxScaler()
    #dfg_norm = pd.DataFrame(scaler.fit_transform(dfg),columns=['degree','counts'])
    #print(dfg_norm.dtypes)
    #print(dfg_norm)
    #RECUPERO LE DUE LISTE DA PLOTTARE 
    #list_occ_norm = dfg_norm[1].tolist()
    #list_gradi_norm = dfg_norm[0].tolist()
    #print (list_occ_norm)
    #print(list_gradi_norm)
    #PLOTTO
    #plt.plot(list_gradi_norm,list_occ_norm)
    #plt.xscale("log")
    #plt.yscale("log")

    #NORMALIZZO CDF
    #pdf
    dfg['pdf'] = dfg['counts'] / sum(dfg['counts'])
    #print(dfg)
    #cdf
    dfg['cdf'] = dfg['pdf'].cumsum()
    dfg = dfg.reset_index()
    print(dfg)
    ax = dfg.plot(x = 'degree', y = 'cdf', grid = True, ax=ax)


    #PLOT GRAFICO NORMALIZZATO 
    #ax = dfg_norm.plot(x='degree',y='counts',kind='line',ax=ax)

    #BOXPLOT
    #bdf[cname[n]] = df['degree']
    #bx = dfg.boxplot()
    #ldf.append(dfg_norm.assign(Location=cname[n]))

    #SCRIVI IL NOME CONTRATTO AL POSTO DEL NUMERO
    patch = mpatches.Patch(color=color, label=cname[n])
    list_patch.append(patch)

#print(map_degree)
#print(dfg)
#print(list_gradi_norm)
#print(list_occ_norm)
#print("Numero nodi : "+str(g.numberOfNodes()))
#i=10078
#print("degree di "+str(i)+" : "+str(list_res[i]))

#PLOTTO LEGENDA E SALVO FILE
plt.xscale('log')
#cdf = pd.concat(ldf)
#print (cdf)
#ax = sns.boxplot(x="Location", y="degree", data=cdf)    #dfg.boxplot(column=['USDT','MGC','LINK','WETH','EOS','BAT','OMG','CPCT','TRX','SHIB'])
plt.xticks(fontsize=12,weight='bold')
plt.yticks(fontsize=12,weight='bold')
#plt.ylabel('DEGREE (normalized)', fontsize=18,weight='bold')
plt.xlabel('DEGREE',fontsize=18,weight='bold')
plt.title('NODES DEGREE DISTRIBUTION',fontsize=18,weight='bold')
f = plt.figure(num=1)
f.set_figheight(10)
f.set_figwidth(10)
plt.legend(fontsize=15,handles=list_patch)    
plt.savefig('./risultati_analisi/cdf_gradi.png')