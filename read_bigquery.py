from google.cloud import bigquery
from google.oauth2 import service_account
import decode

credentials = service_account.Credentials.from_service_account_file(
'/home/lilf4p/Documenti/unipi/tesi-analisi-token/ethereum-blockchain-326613-b9f1ed7669a2.json')

project_id = 'ethereum-blockchain-326613'
client = bigquery.Client(credentials= credentials,project=project_id)

query_job = client.query("""
   SELECT to_address, input
   FROM token_erc20.trx_token10
   LIMIT 100 """)

results = query_job.result() #aspetta che venga completata la query

list_res = [] #lista di coppie (funzione,parametri)
for result in results:
    func_obj,func_params = decode.start(result[0],result[1])
    list_res.append((func_obj,func_params))

print(list_res)