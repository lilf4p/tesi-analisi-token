from google.cloud import bigquery
from google.oauth2 import service_account
import decode
import csv

credentials = service_account.Credentials.from_service_account_file(
'/home/lilf4p/Documenti/unipi/tesi-analisi-token/ethereum-blockchain-326613-b9f1ed7669a2.json')

project_id = 'ethereum-blockchain-326613'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query("""
   SELECT address, from_address, to_address, input, block_timestamp 
   FROM token_erc20.trx_10token
   LIMIT 100 """)

results = query_job.result() #aspetta che venga completata la query

#decodifica input
#list_res = [] #lista di coppie (funzione,parametri)
#for result in results:
#    func_obj,func_params = decode.start(result[0],result[1])
#    list_res.append((func_obj,func_params))
#print(list_res)

#header csv
fieldnames = ['address', 'from_address', 'to_address', 'input', 'block_timestamp']

#apro csv in scrittura
f = open('trx_token.csv','w', encoding='UTF8', newline='')
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()

#scrivo ogni record in una riga
for result in results:
    writer.writerow(result)
    
