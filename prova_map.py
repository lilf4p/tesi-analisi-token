list_contract = ['add1','add2','add3']

#dd = {'add1' : {}, 'add2' : {}, 'add3' : {}}

l=dict()
for ad in list_contract:
    l[ad] = dict()
print(l)

d = l['add1']
d['type1']=1
print(l)

s='type1'
if s in d:
    n = d[s]
    n = n+1
    d[s] = n
else:
    d[s] = 1
    
print(l)