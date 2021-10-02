import config 
from web3 import Web3
import requests
import json

api_key = config.apy_key

#recupero istanza di web3 con infura (va bene infura?)
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/'+config.infura_project_id))
#print(w3.isConnected())

#todo : parsing della tabella, ci interessano questi due campi da riempire 
add_to = w3.toChecksumAddress('0xdac17f958d2ee523a2206206994597c13d831ec7')
input_data = "0xa9059cbb000000000000000000000000b7b0f2c0c007932fb202b994bc6fb1fd51ce9c53000000000000000000000000000000000000000000000000000000174876e800"

#recupero abi tramite richiesta alla api di etherscan 'getapi'
abi_endpoint = f"https://api.etherscan.io/api?module=contract&action=getabi&address={add_to}&apikey={api_key}"
abi = json.loads(requests.get(abi_endpoint).text)

#costruisco il contratto 
contract = w3.eth.contract(address=add_to, abi=abi["result"])

#decodifico -> func_obj : contiene la signature della funzione
#              func_params : json dei parametri della funzione   
func_obj, func_params = contract.decode_function_input(input_data)


print (func_obj)
print (func_params)
    