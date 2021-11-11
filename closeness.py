from matplotlib.colors import Normalize
import networkit as nk
import csv

fo = open('./risultati_analisi/cen_closeness.csv','w')
csv_writer = csv.writer(fo)
for n in range(1,11):
    reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
    fname = './edgelist/edgelist_'+str(n)+'.csv'
    g = reader.read(fname)
    print ("Grafo letto")

    map_nodes = reader.getNodeMap()

    gu = nk.graphtools.toUndirected(g)

    csv_writer.writerow(['contratto '+str(n)])
    csv_writer.writerow(['id_node','value'])
    ac = nk.centrality.TopCloseness(gu,k=20, first_heu=True, sec_heu=False)
    ac.run()
    for id_node,v in zip(ac.topkNodesList(includeTrail=True),ac.topkScoresList(includeTrail=True)):
        for k,value in map_nodes.items():
            if value == id_node:
                id_orig = k
        csv_writer.writerow([id_orig,v])

fo.close()