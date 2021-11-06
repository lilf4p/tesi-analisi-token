import json
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
import pandas as pd 

#"<Function transfer(address,uint256)>"
#"<Function approve(address,uint256)>"
#"<Function transferFrom(address,address,uint256)>"
#"<Function deposit()>"
#"<Function withdraw(uint256)>"

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

fi = open('stats_type_trx.json',"r")

j = json.load(fi)

df = pd.DataFrame(columns=['contratto','transfer','approve','transferFrom','deposit','withdraw','other'])

i=1
z=0
for c,dict_type in j.items():
    type_totali = dict_type['tot']
    list_perc = [cname[i]]

    val = dict_type['<Function transfer(address,uint256)>']
    perc = (int(val)/int(type_totali))*100
    list_perc.append(perc)

    if "<Function approve(address,uint256)>" in dict_type:
        val = dict_type["<Function approve(address,uint256)>"]
        perc = (int(val)/int(type_totali))*100
        list_perc.append(perc)
    else:
        list_perc.append(0)

    if "<Function transferFrom(address,address,uint256)>" in dict_type:
        val = dict_type["<Function transferFrom(address,address,uint256)>"]
        perc = (int(val)/int(type_totali))*100
        list_perc.append(perc)
    else:
        list_perc.append(0)

    if "<Function deposit()>" in dict_type:
        val = dict_type["<Function deposit()>"]
        perc = (int(val)/int(type_totali))*100
        list_perc.append(perc)
    else:
        list_perc.append(0)

    if "<Function withdraw(uint256)>" in dict_type:
        val = dict_type["<Function withdraw(uint256)>"]
        perc = (int(val)/int(type_totali))*100
        list_perc.append(perc)
    else: 
        list_perc.append(0)

    s=0
    for t,v in dict_type.items():
        if (t=='tot' or t=='<Function transfer(address,uint256)>' or t=="<Function approve(address,uint256)>" 
        or t=="<Function transferFrom(address,address,uint256)>" or t=="<Function deposit()>" or t=="<Function withdraw(uint256)>"): continue
        s = s + int(v)   
    
    perc = (s/int(type_totali))*100
    list_perc.append(perc)
    df.loc[z] = list_perc
    z=z+1
    i=i+1

print (df)
#print (df['transfer'].dtypes())
#df=df.astype(float)
df.plot(x='contratto',kind='barh',stacked=True,mark_right=True)
plt.show()
    