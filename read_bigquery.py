from google.cloud import bigquery
from google.oauth2 import service_account
#import decode
import csv

credentials = service_account.Credentials.from_service_account_file(
'ethereum-blockchain-326613-b9f1ed7669a2.json')

project_id = 'ethereum-blockchain-326613'
client = bigquery.Client(credentials= credentials,project=project_id)

#lista dei 10 contratti
list_address = ["0xdac17f958d2ee523a2206206994597c13d831ec7","0x174bfa6600bf90c885c7c01c7031389ed1461ab9","0x514910771af9ca656af840dff83e8264ecf986ca",
"0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2","0x86fa049857e0209aa7d9e616f7eb3b3b78ecfdb0","0x0d8775f648430679a709e98d2b0cb6250d2887ef","0xd26114cd6ee289accf82350c8d8487fedb8a0c07",
"0x8fdcc30eda7e94f1c12ce0280df6cd531e8365c5","0xf230b790e05390fc8295f4d3f60332c93bed42e2","0x95ad61b0a150d79219dcf64e1e6cc01f0b64c4ce"]

#header csv
fieldnames = ['address', 'hash', 'from_address', 'to_address', 'input', 'block_timestamp']

#scrivo header csv e lo apro in append
f = open('trx_token_v2.csv','a', encoding='UTF8', newline='')
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()

#per ogni contratto nella lista, faccio la query e appendo il risultato sul file 
for address in list_address:
   
   query_job = client.query("""
      SELECT address, tabella_trx.hash, from_address, to_address, input, block_timestamp 
      FROM token_erc20.trx_10token as tabella_trx
      WHERE address = '""" + address + """'""")

   results = query_job.result() #aspetta che venga completata la query
   print('Query completata')
   
   #decodifica input
   #list_res = [] #lista di coppie (funzione,parametri)
   #for result in results:
   #    func_obj,func_params = decode.start(result[0],result[1])
   #    list_res.append((func_obj,func_params))
   #print(list_res)

   print('Scrivo il file csv')
   #scrivo ogni record in una riga
   for result in results:
      #func_obj,func_params = decode.start(result[0],result[3])
      writer.writerow(result)
    
f.close