import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import networkit as nk
import pandas as pd

list_patch = []
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

    #RECUPERO LE DUE LISTE DA PLOTTARE 
    list_occ = dfg['counts'].tolist()
    list_size = dfg['size'].tolist()

    #SULLE Y VORREI (NUMERO DI COMPONENTI/COMP TOT)*100
    #NORMALIZZARE
    nc = wc.numberOfComponents()
    list_occ_norm = [((int(occ)/nc)*100) for occ in list_occ]  

    plt.xscale("log")
    plt.xlabel("size of components")
    plt.yscale("log")
    plt.ylabel("number of components")
    plt.plot(list_size,list_occ_norm)
    #SCRIVI NOME CONTRATTO AL POSTO DEL NUMERO
    patch = mpatches.Patch(color=color, label=str(n))
    list_patch.append(patch)

#print(dfg)
#print(wc.numberOfComponents())
plt.legend(handles=list_patch)    
plt.savefig('./risultati_analisi/distr_comp_conn_norm.png')