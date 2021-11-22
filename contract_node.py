import csv 
import os

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

for n in range(1,11):
    foname = './contract_node/node'+str(n)+'.csv'
    os.makedirs(os.path.dirname(foname), exist_ok=True)
    fo = open(foname,'w')
    fieldnames = ['from_address','to_address']
    csv_writer = csv.writer(fo)
    csv_writer.writerow(fieldnames)
    finame = './edgelist/edgelist_'+str(n)+'.csv'
    fi = open (finame,'r')
    csv_reader = csv.reader(fi)
    for row in csv_reader:
        if row[0] == str(n) or row[1] == str(n):
            csv_writer.writerow(row)
