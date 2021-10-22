import csv
import os

#INDICI CONTRATTI 
c1 = "1"
c2 = "2"
c3 = "3"
c4 = "4"
c5 = "5"
c6 = "6"
c7 = "7"
c8 = "8"
c9 = "9"
c10 = "10"

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
    if key not in d: #trx non presente 
        if type_trx == "<Function transfer(address,uint256)>":
            c = "1" #type
        elif "transferFrom" in type_trx:
            c = "2"
        list_arg = [value,value,value,value,time,time,1,c] #lista di [vmin,vmax,vmedia,vsomma,mintime,maxtime,count_trx,type]
        d[key] = list_arg
    else: #trx gia' presente 
        #upgrade values in map for the trx
        #lista di [vmin,vmax,vmedia,vsomma,mintime,maxtime,count_trx,type]
        list_arg = d[key]
        vmin = float(list_arg[0])
        vmax = float(list_arg[1])
        vmedia = float(list_arg[2])
        vsomma = float(list_arg[3])
        mintime = list_arg[4]
        maxtime = list_arg[5]
        count = int(list_arg[6])
    
        #UPGRADE 
        if float(value) < vmin: list_arg[0]=value #vmin
        if float(value) > vmax: list_arg[1]=value #vmax

        #newAve = ((oldAve*oldNumPoints) + x)/(oldNumPoints+1)
        avg = ((vmedia*count) + float(value))/(count+1) #vmedia
        list_arg[2] = str(avg)

        #vsomma
        vsomma = vsomma+float(value) 
        list_arg[3] = str(vsomma)

        if time < list_arg[4]: list_arg[4] = time #mintime
        if time > list_arg[5]: list_arg[5] = time #maxtime

        count = count + 1 #count
        list_arg[6] = str(count)

        if type_trx == "<Function transfer(address,uint256)>":
            list_arg[7] = "1" #type
        elif "transferFrom" in type_trx:
            list_arg[7] = "2"

        d[key] = list_arg

fi.close()

#SCRIVI OGNI DICT SU UN CSV
fieldnames = ['from_address','to_address','val_min','val_max','val_avg','val_sum','time_first','time_last','counter_trx','type_trx']
n=1
for dc in ldict:
    fname = "./trx_contract/trx_contract_"+str(n)+".csv"
    os.makedirs(os.path.dirname(fname), exist_ok=True)
    fo = open(fname,'w', encoding='UTF8', newline='')
    csv_writer = csv.writer(fo)
    csv_writer.writerow(fieldnames)
    for k,v in dc.items():
        ads = str(k).split(',')
        csv_writer.writerow([ads[0],ads[1],v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7]])
    fo.close()
    n=n+1


#ESEMPIO DI AGGREGAZIONE
#293,294,247000000,621000000,412833333.3333333,357000000621000000481000000247000000414000000357000000,2020-07-05 10:36:16+00:00,2020-10-29 09:17:04+00:00,6,"<Function transferFrom(address,address,uint256)>"

#293,294,247000000,621000000,412833333.3333333,2477000000.0,2020-07-05 10:36:16+00:00,2020-10-29 09:17:04+00:00,6,"<Function transferFrom(address,address,uint256)>"
