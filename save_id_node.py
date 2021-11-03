#----------------ID DEI NODI CORRETTI-----------------#
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
##print (idmap)
#try:
#    g = reader.read(fname)
#except: 
#    print("File not exist")
#    exit()
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