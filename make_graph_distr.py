import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import networkit as nk
import matplotlib.ticker as mtick
import pandas as pd
import csv

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

fo = open('./risultati_analisi/media_var_degree.csv','w')
csv_writer = csv.writer(fo)
csv_writer.writerow(['contratto','media','varianza'])

list_patch = []
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
    media = df['degree'].mean()
    var = df['degree'].var()
    csv_writer.writerow([n,media,var])

    #RECUPERO LE DUE LISTE DA PLOTTARE 
    list_occ = dfg['counts'].tolist()
    list_gradi = dfg['degree'].tolist()

    #NORMALIZZARE
    nt = gu.numberOfNodes()
    list_occ_norm = [((int(occ)/nt)*100) for occ in list_occ]

    list_gradi_sorted = sorted(list_gradi)
    max_degree = list_gradi_sorted[-1]
    #print(max_degree)
    list_gradi_norm = [((int(gradi)/int(max_degree))*100) for gradi in list_gradi_sorted]

    #PLOTTO
    plt.xscale("log")
    plt.xlabel("degree")
    plt.yscale("log")
    plt.ylabel("% of nodes")
    plt.plot(list_gradi_norm,list_occ_norm)
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
plt.legend(handles=list_patch)    
plt.savefig('./risultati_analisi/distr_grado_normV1.png')