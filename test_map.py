import csv

key = input("Insert index : ") 

#apri file con mapping add-int
fi = open('map_add-int.csv','r')
csv_reader = csv.reader(fi, delimiter=',')

#carica in struttura dati -- hashmap
mydict = {rows[1]:rows[0] for rows in csv_reader}

print(mydict[key]) #stampa address corrispondente 
