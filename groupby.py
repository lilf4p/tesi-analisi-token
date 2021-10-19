import csv

#INDICI CONTRATTI (DA AGGIORNARE QUANDO SI CAMBIA MAP!!!!!)
c1 = "1"
c2 = "167"
c3 = "363"
c4 = "528"
c5 = "548"
c6 = "703"
c7 = "854"
c8 = "987"
c9 = "1139"
c10 = "1284"

fi = open('trx_token_ottimizzatoV1.csv','r')
csv_reader = csv.reader(fi,delimiter=',')

#LISTA DI 10 DICT, UNA PER CONTRATTO --> SEPARO LE TRX PER CONTRATTO
ldict=[]
for i in range(10):
    ldict.append(dict()) 

#FIELD address,hash,from_address,to_address,input,block_timestamp,value,type

#DIVIDI PER CONTRATTO (ROW[0]==ADD_CONTRATTO)
for row in csv_reader:

    contract_add = row[0]
    from_add = row[2]
    to_add = row[3]
    time = row[5]
    value = row[6]
    type_trx = row[7]

    key = from_add+","+to_add

    #SCELGO IL DICT CORRETTO PER L'INDIRIZZO 
    if contract_add == c1:
        d = ldict[0]
    elif row[0] == c2:
        d = ldict[1]
    elif row[0] == c3:
        d = ldict[2]
    elif row[0] == c4:
        d = ldict[3]
    elif row[0] == c5:
        d = ldict[4]
    elif row[0] == c6:
        d = ldict[5]
    elif row[0] == c7:
        d = ldict[6]
    elif row[0] == c8:
        d = ldict[7]
    elif row[0] == c9:
        d = ldict[8]
    elif row[0] == c10:
        d = ldict[9]
    else: continue

    #SE COPPIA (ADD_TO,ADD_FROM) IS NOT IN KEYS AGGIUNGI
    #ALTRIMENTI AGGIORNA I VALORI
    if key not in d.keys(): #trx non presente 
        list_arg = [value,value,value,value,time,time,1,type_trx] #lista di [vmin,vmax,vmedia,vsomma,mintime,maxtime,count_trx,type]
        d[key] = list_arg
    else: #trx gia' presente 
        #upgrade values in map for the trx
        #lista di [vmin,vmax,vmedia,vsomma,mintime,maxtime,count_trx,type]
        list_arg = d[key]
        #print(list_arg)
        if value < list_arg[0]: list_arg[0]=value #vmin
        if value > list_arg[1]: list_arg[1]=value #vmax
        #newAve = ((oldAve*oldNumPoints) + x)/(oldNumPoints+1)
        avg = ((int(list_arg[2])*int(list_arg[6])) + int(value))/(int(list_arg[6])+1) #vmedia
        list_arg[2] = str(avg)
        list_arg[3] = list_arg[3]+value #vsomma
        if time < list_arg[4]: list_arg[4] = time #mintime
        if time > list_arg[5]: list_arg[5] = time #maxtime
        list_arg[6] = list_arg[6] + 1 #count
        list_arg[7] = type_trx #type

        d[key] = list_arg

fi.close()

#SCRIVI OGNI DICT SU UN CSV
fieldnames = ['val_min','val_max','val_avg','val_sum','time_first','time_last','counter_trx','type_trx']
n=1
for dc in ldict:
    fname = "trx_contract_"+str(n)+".csv"
    fo = open(fname,'w', encoding='UTF8', newline='')
    csv_writer = csv.writer(fo)
    csv_writer.writerow(fieldnames)
    for k,v in dc.items():
        ads = str(k).split(',')
        csv_writer.writerow([ads[0],ads[1],v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7]])
    fo.close()
    n=n+1

