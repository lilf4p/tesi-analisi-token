#COSTRUZIONE GRAFO CON NETWORKIT E VARIE PROVE
import matplotlib
matplotlib.use('agg')
from graph_tool.all import *
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.isomorphism.ismags import partition_to_color
from networkx.drawing.layout import random_layout
import networkit as nk
import pandas as pd
import csv

n=3
#-----------NETWORKIT--------------#
reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
g = reader.read('./edgelist/edgelist_'+str(n)+'.csv')
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
gu = nk.graphtools.toUndirected(g)
#newGraph = nk.components.ConnectedComponents.extractLargestConnectedComponent(gu, True)
#nk.viztasks.drawGraph(newGraph)
#plt.show()
#CALCOLA DEGREE
#dd = nk.centrality.DegreeCentrality(gu).run()
#list_res = dd.ranking()
#coreDec = nk.centrality.CoreDecomposition(gu)
#coreDec.run()
#print(set(coreDec.scores()))
#nk.viztasks.drawGraph(g, node_size=[(k**2)*20 for k in coreDec.scores()])
#plt.show()    
#COMP CONN MAGGIORE 
newGraph = nk.components.ConnectedComponents.extractLargestConnectedComponent(gu, True)
#gx = nk.nxadapter.nk2nx(newGraph)
#fname = open ('./risultati_analisi/grafi_conn/graph'+str(n)+'_conn.graphml','w')
#nk.GraphMLIO.GraphMLWriter.write(g,fname)
nk.writeGraph(newGraph,'./risultati_analisi/grafi_conn/graph'+str(n)+'_conn.graphml',nk.Format.GraphML)
gc = load_graph('./risultati_analisi/grafi_conn/graph'+str(n)+'_conn.graphml')
pos = sfdp_layout(gc)
graph_draw(gc,pos,output_size=(1000,1000),output='./risultati_analisi/grafi_conn/graph_'+str(n)+'_conn.pdf')

#wc = nk.components.WeaklyConnectedComponents(g).run() 
#print ("Numero di componenti weakly connected del grafo "+str(n)+": "+str(wc.numberOfComponents()))
#dict_comp = wc.getComponentSizes() #Returns a map with the component indexes as keys, and their size as values

#plt.xscale("log")
#plt.xlabel("size of components")
#plt.yscale("log")
#plt.ylabel("number of components")
#plt.plot(list_scores)
#plt.savefig('distr_comp_conn_1.png')


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