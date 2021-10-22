import csv
import config
from web3 import Web3
import json
import requests
import time

# --------- CREO I 10 C0NTRATTI PER DECODIFICARE -------- #
api_key = config.apy_key
#recupero istanza di web3 con infura 
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/'+config.infura_project_id))
#print(w3.isConnected())
list_contract = ["0xdac17f958d2ee523a2206206994597c13d831ec7","0x174bfa6600bf90c885c7c01c7031389ed1461ab9",
"0x514910771af9ca656af840dff83e8264ecf986ca","0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2","0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0",
"0x0d8775f648430679a709e98d2b0cb6250d2887ef","0xd26114cd6ee289accf82350c8d8487fedb8a0c07",
"0x8fdcc30eda7e94f1c12ce0280df6cd531e8365c5","0xf230b790e05390fc8295f4d3f60332c93bed42e2","0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce"]
map_contract = dict()
for add in list_contract:
    #recupero abi tramite richiesta alla api di etherscan 'getapi'
    abi_endpoint = f"https://api.etherscan.io/api?module=contract&action=getabi&address={add}&apikey={api_key}"
    abi = json.loads(requests.get(abi_endpoint).text)
    #costruisco il contratto 
    contract = w3.eth.contract(address=w3.toChecksumAddress(add), abi=abi["result"])
    map_contract[add] = contract
#----------------------------------------------------------#

print ("Scaricate abi dei contratti")

# file vecchio
fi = open('trx_token_v2.csv','r')
csv_reader = csv.reader(fi, delimiter=',')

fieldnames = ['address', 'hash', 'from_address', 'to_address', 'input', 'block_timestamp', 'value', 'type']
# file editato
fo = open('trx_token_ottimizzatoV1.csv','w', encoding='UTF8', newline='')
csv_writer = csv.writer(fo)

map_add = dict()
index = 1
#mappa gli add dei contratti
for ad in list_contract:
    map_add[ad] = index
    index = index+1

start_time = time.time()
for row in csv_reader:
    #print(row)
    # skippa header csv
    if (row[0] != "address"): 
        # decode(input) -> scrivi sul file nuovo solo se e' TRANSFER/TRANSFER_TO

        try: #CATTURA ECCEZIONE DATA DALLA CHIAMATA DI DECODE SU VALORI DI INPUT NON VALIDI --> SONO TRX FALLITE 
            func_obj, func_params = map_contract[row[0]].decode_function_input(row[4])
        except: continue

        if (str(func_obj) == "<Function transfer(address,uint256)>" or ("transferFrom" in str(func_obj))):
            #print(func_obj)
            #print(func_params)
            #print("ITER")
            # mappa row[0]
            if row[0] in map_add:
                row[0] = map_add[row[0]]
            else: 
                map_add[row[0]] = index
                row[0]=index
                index = index+1
            # mappa row[2]
            if row[2] in map_add:
                row[2] = map_add[row[2]]
            else: 
                map_add[row[2]] = index
                row[2]=index
                index = index+1
            # row[3] = decode(input)[to] -- nella quarta colonna (address_to) inserisco il valore _to ottenuto decodificando input 
            if (str(func_obj) == "<Function transfer(address,uint256)>"): 
                row[3] = list(func_params.values())[0] # se funzione transfer devo prendere il primo parametro
                value = list(func_params.values())[1]
            elif "transferFrom" in str(func_obj):
                row[3] = list(func_params.values())[1] # se funzione transferFrom prendo il secondo
                value = list(func_params.values())[2]
            # map row[3]
            if row[3] in map_add:
                row[3] = map_add[row[3]]
            else:
                map_add[row[3]] = index
                row[3]=index
                index = index+1
            #scrivi nuova riga sul file nuovo
            row.append(value)
            row.append(func_obj)
            csv_writer.writerow(row)
               
    else: csv_writer.writerow(fieldnames)

fi.close()
fo.close()
print("--- %s seconds ---" % (time.time() - start_time))

# scrivi map su file 
#print(map_add)
fmap = open('map_add-int.csv','w', encoding='UTF8', newline='')
csv_writer2 = csv.writer(fmap)
csv_writer2.writerow(['address','index'])
for key, value in map_add.items():
    csv_writer2.writerow([key,value])

fmap.close()
