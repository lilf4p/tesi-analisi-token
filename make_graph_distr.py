import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import networkit as nk
import matplotlib.ticker as mtick
import pandas as pd


list_patch = []
for color,n in zip(mcolors.TABLEAU_COLORS,range(1,11)):
    fname = "./edgelist/edgelist_"+str(n)+".csv"
    reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
    try:
        g = reader.read(fname)
    except: 
        print("File not exist")
        exit()
    dd = nk.centrality.DegreeCentrality(g,normalized=True).run()
    list_res = dd.ranking()
    
    #GROUPBY(VALORE)
    df = pd.DataFrame(list_res,columns=['id_node','degree'])
    dfg = df.groupby(['degree']).size().reset_index(name='counts')
    
    #RECUPERO LE DUE LISTE DA PLOTTARE 
    list_occ = dfg['counts'].tolist()
    list_gradi = dfg['degree'].tolist()

    #NORMALIZZARE
    nt = g.numberOfNodes()
    list_occ_norm = [((int(occ)/nt)*100) for occ in list_occ]
    list_gradi = sorted(list_gradi)    
    #PLOTTO
    plt.xscale("log")
    plt.xlabel("degree")
    plt.yscale("log")
    plt.ylabel("% of nodes")
    plt.plot(list_gradi,list_occ_norm)
    #SCRIVI IL NOME CONTRATTO AL POSTO DEL NUMERO
    patch = mpatches.Patch(color=color, label=str(n))
    list_patch.append(patch)

#print(map_degree)
#print(dfg)

#print("Numero nodi : "+str(g.numberOfNodes()))
#i=10078
#print("degree di "+str(i)+" : "+str(list_res[i]))

#PLOTTO LEGENDA E SALVO FILE
plt.legend(handles=list_patch)    
plt.savefig('./risultati_analisi/distr_grado_normV1.png')