import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import networkit as nk
import pandas as pd

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

list_patch = []
z=0
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

    #RECUPERO LE DUE LISTE DA PLOTTARE 
    list_occ = dfg['counts'].tolist()
    list_size = dfg['size'].tolist()

    #SULLE Y VORREI (NUMERO DI COMPONENTI/COMP TOT)*100
    #NORMALIZZARE
    nc = wc.numberOfComponents()
    list_occ_norm = [((int(occ)/nc)*100) for occ in list_occ]
    list_size_ord = sorted(list_size)
    max_size = list_size_ord[-1]
    list_size_norm = [((int(sz)/max_size)*100) for sz in list_size_ord]

    #RECUPERA LE 10 COMPONENTI CON SIZE MAGGIORE
    #first_5comp = list_occ_norm[:4]
    #k = (len(list_size_ord) - 4)
    #other_comp = list_occ_norm[-k:]
    #print(dfg)
    #print(list_occ[:4])
    
    #row = [cname[n]]
    #for s in first_5comp:
    #    row.append(s)
    #sum = 0
    #for s in other_comp:
    #    sum = sum + s
    #row.append(sum)
    #ndf.loc[z] = row
    #z=z+1

    #label=[]
    #for i in range(4):
    #    st = list_occ[i]
    #    df_tmp = dfg.query("counts=="+str(st))
    #    label.append(df_tmp["size"].iloc[0])
    #label.append("others")
    #labels.append(label)
    #print(labels)

    #print(list_size_ord)
    #print()
    #print(first_10size) 
    #print()
    #print(other_size)



    plt.xscale("log")
    plt.xlabel("size of components")
    plt.yscale("log")
    plt.ylabel("number of components")
    plt.plot(list_size_norm,list_occ_norm)
    #SCRIVI NOME CONTRATTO AL POSTO DEL NUMERO
    patch = mpatches.Patch(color=color, label=cname[n])
    list_patch.append(patch)

#print(ndf)
#ax = ndf.plot(x='contratto',ylabel="% occorrenze size",kind='bar',stacked=True,mark_right=True,figsize=(12, 8), rot='horizontal')
#n=0
#for c in ax.containers:
    # Optional: if the segment is small or 0, customize the labels
#    l = labels[n]
#    lbl = [l[0],l[1],l[2],l[3]]
#    print(lbl)
    # remove the labels parameter if it's not needed for customized labels
#    ax.bar_label(c, fmt='%0.0f', label_type='center',fontsize=7, labels=lbl)
#    n=n+1

plt.legend(handles=list_patch)    
plt.savefig('./risultati_analisi/grafico_comp_conn.png')
#print(wc.numberOfComponents())
#plt.savefig('./risultati_analisi/istog_comp_conn.png')