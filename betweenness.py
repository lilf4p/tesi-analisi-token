import networkit as nk
import csv

fo = open('./risultati_analisi/cen_betweenness.csv','w')
csv_writer = csv.writer(fo)
for n in range(1,11):
    reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
    fname = './edgelist/edgelist_'+str(n)+'.csv'
    g = reader.read(fname)
    print ("Grafo letto")

    map_nodes = reader.getNodeMap()

    #VALORI DI CENTRALITA' 

    gu = nk.graphtools.toUndirected(g)
    #print(gu.isDirected())
    #APPROXIMATION OF BETWEENNESS   
    csv_writer.writerow(['contratto '+str(n)])
    csv_writer.writerow(['id_node','value'])
    abc = nk.centrality.Betweenness(gu)
    abc.run()
    for id_node,v in abc.ranking()[:10]:
        for k,value in map_nodes.items():
            if value == id_node:
                id_orig = k
        csv_writer.writerow([id_orig,v])

fo.close()

#EIGEVECTOR
#ec = nk.centrality.EigenvectorCentrality(g)
#ec.run()
#print(ec.ranking()[:10]) # the 10 most central nodes

#PAGERANK
#pr = nk.centrality.PageRank(g, 1e-6)
#pr.run()
#print(pr.ranking()[:10]) # the 10 most central nodes