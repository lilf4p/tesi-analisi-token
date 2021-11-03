#CALCOLA A PARTIRE DAL FILE JSON stats_type_trx.json LA PERCENTUALE DI LOSS DI TRX OTTENUTA DOPO L'OTTIMIZZAZIONE DEL FILE GREZZO

import json

fi = open('stats_type_trx.json',"r")

d = json.load(fi)

for c,dict_type in d.items():
    type_scartati = 0
    type_totali = dict_type['tot']
    for t,v in dict_type.items():
        if t == 'tot' or t == '<Function transfer(address,uint256)>' or t == '<Function transferFrom(address,address,uint256)>': continue
        else: 
            type_scartati = type_scartati+int(v)
    
    print(c+":"+str((type_scartati/type_totali)*100
    ))