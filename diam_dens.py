#CALCOLA DIAMETRO E DENSITA' DEL GRAFO DI TUTTI I CONTRRATTI
#E LO SCRIVE SU UN CSV 
# 'CONTRATTO' 'DIAMETRO' 'DENSITA'

import csv
import networkit as nk

fo = open ('./risultati_analisi/diam_dens.csv','w')
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
    #PRIMA CALCOLA DISTANZE GRAFO
    gu = nk.graphtools.toUndirected(g)
    #print(gu.isConnected())
    diam = nk.distance.Diameter(gu,algo=1)
    diam.run()
    d = diam.getDiameter()
    
    #DENSITA'
    dens = nk.graphtools.density(gu)

    csv_writer.writerow([n,d,dens])
    
fo.close()
