import networkit as nk
import csv

fo = open('./risultati_analisi/val_centrality.csv','w')
csv_writer = csv.writer(fo)

reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
g = reader.read('./edgelist/edgelist_1.csv')
print ("Grafo letto")

map_nodes = reader.getNodeMap()

#VALORI DI CENTRALITA' 

#APPROXIMATION OF BETWEENNESS   
csv_writer.writerow(['APPROXIMATUION BETWEENNESS'])
csv_writer.writerow(['id_node','value'])
abc = nk.centrality.ApproxBetweenness(g, epsilon=0.1)
abc.run()
for id_node,v in abc.ranking()[:10]:
    for k,value in map_nodes.items():
        if value == id_node:
            id_orig = k
    csv_writer.writerow([id_orig,v])

#EIGEVECTOR
#ec = nk.centrality.EigenvectorCentrality(g)
#ec.run()
#print(ec.ranking()[:10]) # the 10 most central nodes

#PAGERANK
#pr = nk.centrality.PageRank(g, 1e-6)
#pr.run()
#print(pr.ranking()[:10]) # the 10 most central nodes