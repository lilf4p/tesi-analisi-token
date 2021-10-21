import networkx as nx
import matplotlib.pyplot as plt

f = open('./trx_contract/trx_contract_1.csv',"r")
next(f,None)
Graphtype = nx.Graph()
G = nx.read_edgelist(f, delimiter=',', create_using=Graphtype, nodetype=int, data=(("vmin",str),("vmax",str),("vavg",str),("vsum",str),("mintime",str),("maxtime",str),("count",str),("type",str),))

pos = nx.random_layout(G)
nx.draw(G,pos)
nx.draw_networkx_edge_labels(G, pos)
#print(G)

plt.show()