import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

cname = {1:"USDT", 2:"MGC", 3:"LINK", 4:"WETH", 5:"EOS", 6:"BAT", 7:"OMG", 8:"CPCT", 9:"TRX", 10:"SHIB"}

df = pd.read_csv('./risultati_analisi/diam_dens.csv')

df["contratto"] = ['USDT','MGC','LINK','WETH','EOS','BAT','OMG','CPCT','TRX','SHIB']
print(df)

ax = df.plot.bar(x='contratto',y='diam')
plt.xticks(fontsize=14,weight='bold')
plt.yticks(fontsize=14,weight='bold')
plt.xlabel('CONTRACTS',fontsize=16,weight='bold')
plt.ylabel('DIAMETERS',fontsize=16,weight='bold')
plt.title('DIAMETER',fontsize=18,weight='bold')
ax.get_legend().remove()
f = plt.figure(num=1)
f.set_figheight(10)
f.set_figwidth(10)
plt.savefig('./risultati_analisi/diam.png')