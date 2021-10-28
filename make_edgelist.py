#CREA 10 EDGELIST SENZA PESI -- SOLO NODI FROM->TO
import pandas as pd
import time as tm
import os

st = tm.time()
for n in range(1,11):
    fname = ("./trx_contract/trx_contract_"+str(n)+".csv")
    columns = ['from_address','to_address']
    df = pd.read_csv(fname)[columns]
    os.makedirs(os.path.dirname('./edgelist/edgelist_'+str(n)+'.csv'), exist_ok=True)
    df.to_csv(r'./edgelist/edgelist_'+str(n)+'.csv', index = False)

print("--- %s seconds ---" % (tm.time() - st))

