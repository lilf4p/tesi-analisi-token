#CALCOLA DIAMETRO E DENSITA' DEL GRAFO DI TUTTI I CONTRRATTI
#E LO SCRIVE SU UN CSV 
# 'CONTRATTO' 'DIAMETRO' 'DENSITA'

import csv
import networkit as nk

fo = open ('./risultati_analisi/diam_dens1.csv','w')
csv_writer = csv.writer(fo)
csv_writer.writerow(['contratto','diam','dens'])

for n in range(1,11):
    fname = "./edgelist/edgelist_"+str(n)+".csv"
    reader = nk.graphio.EdgeListReader(',',1,'#',directed=True,continuous=False)
    try:
        g = reader.read(fname)
    except: 
        print("File not exist")
        exit()
    map_nodes = reader.getNodeMap()

    #DIAMETRO
    gu = nk.graphtools.toUndirected(g)
    #print(g.numberOfNodes())

    # Extract largest connect component
    newGraph = nk.components.ConnectedComponents.extractLargestConnectedComponent(gu, True)
    #print(newGraph.numberOfNodes())
    
    #FANNO LA STESSA COSA WEAKLY SU GRAFO DIRETTO E CONNECTED SU GRAFO NON DIRETTO
    #print(nk.components.ConnectedComponents(gu).run().numberOfComponents())
    #print(nk.components.WeaklyConnectedComponents(g).run().numberOfComponents())

    diam = nk.distance.Diameter(newGraph,algo=1)
    diam.run()
    d,scarta = diam.getDiameter()
    #print(d)
    
    #DENSITA'
    dens = nk.graphtools.density(gu)

    csv_writer.writerow([n,d,dens])
    
fo.close()
