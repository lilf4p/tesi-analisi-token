import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import networkit as nk

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
    print ("Numero di componenti weakly connected del grafo "+str(n)+": "+str(wc.numberOfComponents()))
    dict_comp = wc.getComponentSizes() #Returns a map with the component indexes as keys, and their size as values
    #list_comp = sorted(dict_comp.items())
    #x,y = zip(*list_comp)
    list_scores = sorted(list(dict_comp.values()),reverse=True)
    #print (list_scores)
    plt.xscale("log")
    plt.xlabel("size of components")
    plt.yscale("log")
    plt.ylabel("number of components")
    plt.plot(list_scores)
    patch = mpatches.Patch(color=color, label=str(n))
    list_patch.append(patch)

plt.legend(handles=list_patch)    
plt.savefig('distr_comp_conn.png')