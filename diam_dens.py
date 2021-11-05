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
    diam = nk.distance.Diameter(g).getDiameter()
    a,b = diam
    #print(a,b)
    for k,value in map_nodes.items():
        if value == a:
            ida = k
        if value == b:
            idb = k 

    #DENSITA'
    dens = nk.graphtools.density(g)

    csv_writer.writerow([n,str(ida)+"->"+str(idb),dens])
    
fo.close()
