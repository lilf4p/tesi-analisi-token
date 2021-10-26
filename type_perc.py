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
fi = open('trx_token_piccolo.csv','r')
csv_reader = csv.reader(fi, delimiter=',')

#lista di dict di type-counter
l=dict()
for ad in list_contract:
    l[ad] = dict(tot=0)
#print(l)
start_time = time.time()
for row in csv_reader:
    #print(row)
    # skippa header csv
    if (row[0] != "address"): 
        # decode(input) 

        try: #CATTURA ECCEZIONE DATA DALLA CHIAMATA DI DECODE SU VALORI DI INPUT NON VALIDI --> SONO TRX FALLITE 
            func_obj, func_params = map_contract[row[0]].decode_function_input(row[4])
        except: continue

        d = l[row[0]]

        d['tot'] = d['tot'] + 1

        if str(func_obj) in d:
            n = d[str(func_obj)]
            n = n+1
            d[str(func_obj)] = n
        else:
            d[str(func_obj)] = 1
            
        #print(l)
             
fi.close()


fo = open ('stats_type_trx.json','w')
json.dump(l,fo,indent=4)

print("--- %s seconds ---" % (time.time() - start_time))



#print(l)
