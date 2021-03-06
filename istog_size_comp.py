import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors as mcolors
import networkit as nk
import pandas as pd

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

list_patch = []
z=0
labels = [[],[],[],[],[],[],[],[],[]]
ndf = pd.DataFrame(columns=['contracts','1','2','3','4','5','6','7','8','other'])
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

    df = pd.DataFrame(list(dict_comp.items()),columns=['id_comp','size'])

    list_size = sorted(list(dict_comp.values()),reverse=True)

    #SPLITTA IN DUE LISTE UNA CON LE PRIME K SIZE, UNA CON LE ALTRE 
    k=8
    ksizes = list_size[:k]
    othersizes = list_size[-(len(list_size)-k):]

    #RIGA DEL DF DA PLOTTARE 
    row = [cname[n]]

    tot_nodi = g.numberOfNodes()
    #CALCOLA PERCENTUALI KSIZES
    for s in ksizes:
        perc = (int(s)/tot_nodi)*100
        row.append(perc)
    
    #PERC OTHER
    sum = 0
    for s in othersizes:
        sum = sum+int(s)
    perc = (int(sum)/tot_nodi)*100
    row.append(perc)

    ndf.loc[z] = row
    z=z+1

    print(ksizes)
    #w=0
    #for w in range(8):
    #    labels[w].append(ksizes[w])
    #labels[8].append('others')

print(tot_nodi)
print(ndf)
ax = ndf.plot(x='contracts',ylabel="% nodes",kind='bar',stacked=True,mark_right=False,rot='horizontal')

#print(labels)
#for c in ax.containers:
    
# customize the label to account for cases when there might not be a bar section
#n=0
#for c in ax.containers:
#    lbl = labels[n]
#    t = 0
#    print(lbl)
#    for v in c:
#        print(t)
#        if ((w := v.get_height()) < 2) and (lbl[t] != 'others'): 
#            lbl[t]=''
#        t=t+1
#        print(lbl)
#    ax.bar_label(c, label_type='center',fontsize=10, labels=lbl, weight='bold')
#    n=n+1

# ESTETICA DEL GRAFICO PLOTTATO

plt.xticks(fontsize=12,weight='bold')
plt.yticks(fontsize=12,weight='bold')
plt.ylabel('% NODES', fontsize=18,weight='bold')
plt.xlabel('CONTRACTS',fontsize=18,weight='bold')
patch = mpatches.Patch(color='tab:olive', label='others')
list_patch.append(patch)
plt.legend(fontsize=17,handles=list_patch)

f = plt.figure(num=1)
f.set_figheight(12)
f.set_figwidth(10)
plt.savefig('./risultati_analisi/istog_size_comp1.png')
#plt.show()

#print(list_size)
#print("KSIZES")
#print(ksizes)
#print("OTHERSIZES")
#print(othersizes)
    
