#COSTRUZIONE GRAFO CON NETWORKIT E VARIE PROVE

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism.ismags import partition_to_color
from networkx.drawing.layout import random_layout
import networkit as nk
import pandas as pd
import csv
 
#-----------NETWORKIT--------------#

reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
g = reader.read('./edgelist/edgelist_1.csv')

#----------MAP DEI NODI ESEGUITO DA NETWORKIT QUANDO CREA UN GRAFO--------------#
map_nodes = reader.getNodeMap()

i = 0
for u, v in g.iterEdges():
    if i > 10:
        print('...')
        break
    for k,value in map_nodes.items():
        if value == u:
            idu = k
        elif value == v:
            idv = k

    print(str(u)+'(:'+str(idu)+')', str(v)+'(:'+str(idv)+')')
    i += 1
#-------------------------------------------------------------#

#nk.viztasks.drawGraph(g)

#DIAMETRO
diam = nk.distance.Diameter(g).getDiameter()
a,b = diam
#print(a,b)
for k,value in map_nodes.items():
    if value == a:
        ida = k
    if value == b:
        idb = k 
print(str(ida)+"->"+str(idb))  

#DENSITA'
print(nk.graphtools.density(g))

################IMPLEMENTATA A MANO###############
#----------------MAP DEI NODI ESEGUITO DA NETWORKIT QUANDO CREA UN GRAFO-----------------#
# Get mapping from node ids in nxG to node ids in G
#f = open(fname,'r')
#csv_reader = csv.reader(f,delimiter=',')
#next(csv_reader)
#list_node_id = []
#for row in csv_reader:
#    list_node_id.append(row[0])
#    list_node_id.append(row[1])
#print(range(len(list_node_id)))
#idmap = dict((id, u) for (id, u) in zip(range(len(list_node_id)), list_node_id))
#idmap = dict()
#idnew = 0
#for idold in list_node_id:
#    if idold in idmap : continue
#    else : 
#        idmap[idold] = idnew
#        idnew = idnew + 1
#
#print (idmap)
#i = 0
#for u, v in g.iterEdges():
#    if i > 10:
#        print('...')
#        break
#    for k,value in idmap.items():
#        if value == u:
#            idu = k
#        elif value == v:
#            idv = k
#
#    print(str(u)+'(:'+str(idu)+')', str(v)+'(:'+str(idv)+')')
#    i += 1
#----------------------------------------------------#
###########################################

#-----------FUNZIONI UTILI PER MISURE---------------# 

#nk.stats.gini() -- CAPIRE CHE ARGOMENTO VUOLE 

#CENTRALITA'
#abc = nk.centrality.ApproxBetweenness(g, epsilon=0.1)
#abc.run()
#print(abc.ranking()[:10])

#----------------------------------------#

####################################
#          PROVE VARIE             #
####################################

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