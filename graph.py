import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.layout import random_layout

f = open('./trx_contract/trx_contract_10.csv',"r")
next(f,None)
Graphtype = nx.Graph()
G = nx.read_edgelist(f, delimiter=',', create_using=Graphtype, nodetype=int, data=(("vmin",str),("vmax",str),("vavg",str),("vsum",str),("mintime",str),("maxtime",str),("count",str),("type",str),))

#pos = nx.nx_agraph.graphviz_layout(G,prog="sfdp")
pos = random_layout(G)
nx.draw(G,pos)
nx.draw_networkx_labels(G, pos)
#print(G)

#nx.write_gexf(G, "test.gexf")
plt.show()