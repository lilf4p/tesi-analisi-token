import csv

fo = open("count_trx_multiple.csv",'w')
csv_writer = csv.writer(fo)
csv_writer.writerow(['contract','trx_multiple','trx_tot'])

for n in range(1,11):
    fname = "./trx_contract/trx_contract_riprova_"+str(n)+".csv"
    fi = open(fname,"r")
    print(fi.name)
    csv_reader = csv.reader(fi,delimiter=',')
    count_multi_trx = 0
    tot = 0
    next(csv_reader)
    for row in csv_reader:
        tot = tot+1
        if (int(row[8])>1): 
            count_multi_trx = count_multi_trx + 1
    csv_writer.writerow([n,count_multi_trx,tot])
    fi.close()

fo.close()
    