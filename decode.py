
#funzione di decodifica del campo input di una transazione 
#   (add_to, input_data) -> decodifica(input_data) con decodifica == forma leggibile 

import config 
from web3 import Web3
import requests
import json

def start(add_to, input_data) : 

    api_key = config.apy_key

    #recupero istanza di web3 con infura (va bene infura?)
    w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/'+config.infura_project_id))
    #print(w3.isConnected())

    #recupero abi tramite richiesta alla api di etherscan 'getapi'
    abi_endpoint = f"https://api.etherscan.io/api?module=contract&action=getabi&address={add_to}&apikey={api_key}"
    abi = json.loads(requests.get(abi_endpoint).text)

    #costruisco il contratto 
    contract = w3.eth.contract(address=w3.toChecksumAddress(add_to), abi=abi["result"])

    #decodifico -> func_obj : contiene la signature della funzione
    #              func_params : json dei parametri della funzione   
    func_obj, func_params = contract.decode_function_input(input_data)

    return func_obj,func_params