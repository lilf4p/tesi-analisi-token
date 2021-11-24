import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from graph_tool.all import *
import numpy as np 


G = load_graph_from_csv('./trx_contract/trx_contract_1.csv',directed=True,skip_first=True)

print(G)
print(G.list_properties())

vprop = G.vp['name']
eprop = G.ep['val_sum']

n=0
for e in G.edges():
    v,u = e
    if n==10: break
    print(str(v)+'('+str(vprop[v])+'),'+str(u)+'('+str(vprop[u])+'),'+str(eprop[e]))
    n+=1

#deg = G.degree_property_map("total")


