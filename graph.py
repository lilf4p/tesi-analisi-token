import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism.ismags import partition_to_color
from networkx.drawing.layout import random_layout
import networkit as nk
import pandas as pd
 
fname = input("NOME FILE : ")

#-----------NETWORKIT--------------#
#lavora con edgelist

reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
try:
    g = reader.read(fname)
except: 
    print("File non esiste!")
    exit()
nk.overview(g)
i = 0
for u, v in g.iterEdges():
    if i > 5:
        print('...')
        break
    print(u, v)
    i += 1
#FUNZIONI UTILI PER MISURE 

#nk.stats.gini() -- CAPIRE CHE ARGOMENTO VUOLE 

#COMPONENTI CONNESSE 
#cc = nk.components.StronglyConnectedComponents(g)
#cc.run()
#print("number of components ", cc.numberOfComponents())

#DISTRIBUZIONE GRADO NODI CON GRAFICO
dd = sorted(nk.centrality.DegreeCentrality(g).run().scores(), reverse=True)
plt.xscale("log")
plt.xlabel("degree")
plt.yscale("log")
plt.ylabel("number of nodes")
plt.plot(dd)
plt.show()

#CENTRALITA'
#abc = nk.centrality.ApproxBetweenness(g, epsilon=0.1)
#abc.run()
#print(abc.ranking()[:10])

#----------------------------------------#







#--------------PROVA NETWORKX------------#
#f = open('./trx_contract/trx_contract_1.csv',"r")
#next(f,None)
#Graphtype = nx.Graph()
#G = nx.read_edgelist(f, delimiter=',', create_using=Graphtype, nodetype=int, data=(("vmin",str),("vmax",str),("vavg",str),("vsum",str),("mintime",str),("maxtime",str),("count",str),("type",str),))

#print(G)

#pos = nx.nx_agraph.graphviz_layout(G,prog="sfdp")
#pos = random_layout(G)
#nx.draw(G,pos)
#nx.draw_networkx_labels(G, pos)
#print(G)

#nx.write_gexf(G, "test.gexf")
#plt.show()
#-----------------------------------------#

#------------PROVA PANDAS-----------#

#definisci un sottoinsieme di colonne (prima riga csv)
#columns = ['from_address','to_address','val_min']

#df = pd.read_csv('./trx_contract/trx_contract_4.csv')[columns]

#print(df.shape)
#print(df.columns)
#print(df.head(5))
#print(df.dtypes)

#RIDUCE DIMENSIONE DATAFRAME!!!
#df = df.astype('category')

#G = nx.from_pandas_edgelist(df,'from_address','to_address')
#print(nx.info(G))
#---------------------------------------#