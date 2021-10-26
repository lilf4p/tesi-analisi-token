
import csv

tot=0
for n in range(1,11):
    fname = "./trx_contract/trx_contract_"+str(n)+".csv"
    fi = open(fname,"r")
    print(fi.name)
    csv_reader = csv.reader(fi,delimiter=',')
    count = 0
    for row in csv_reader:
        if row[0] == 'from_address': continue
        else: 
            count = count + int(row[8])
    
    print(count)
    tot = tot + count
    
print('-------trx totali: '+str(tot)+'-------')