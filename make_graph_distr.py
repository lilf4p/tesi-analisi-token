import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import networkit as nk

list_patch = []
for color,n in zip(mcolors.TABLEAU_COLORS,range(1,11)):
    fname = "./edgelist/edgelist_"+str(n)+".csv"
    reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
    try:
        g = reader.read(fname)
    except: 
        print("File not exist")
        exit()
    dd = sorted(nk.centrality.DegreeCentrality(g).run().scores(), reverse=True)
    #print (dd)
    plt.xscale("log")
    plt.xlabel("degree")
    plt.yscale("log")
    plt.ylabel("number of nodes")
    plt.plot(dd)
    patch = mpatches.Patch(color=color, label=str(n))
    list_patch.append(patch)

plt.legend(handles=list_patch)    
plt.savefig('distr_grado_tot_v2.png')