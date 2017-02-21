# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:37:34 2017

@author: theov
"""

import json,io, codecs

with open('$HOME/NoSQLTheoVleeschouwers/farmermarket.json') as jsonfile:
    data = json.load(jsonfile)
column = ["id","adress","quarter","city","zip code","long","lat"]
market = data["data"]
i = 0
market2 = {}
market2['market'] = []
while i < len(market) :
    liste = market[i]
    li = "012345678"
    for j in li :
        liste.remove(liste[1])
    market2['market'].append({ 
        column[0] : str(liste[0]),  
        column[1] : str(liste[1]),
        column[2] : str(liste[2]),
        column[3] : str(liste[3]),
        column[4] : str(liste[4]),
        column[5] : str(liste[5]),
        column[6] : str(liste[6])
})
    i+=1 


with open('$HOME/NoSQLTheoVleeschouwers/market_clean.json', 'w') as f:
    json.dump(market2,f)
    
    
    
    
with open('$HOME/NoSQLTheoVleeschouwers/EStores.json') as jsonfile:
    estore = json.load(jsonfile)
column2 = ["id","type","name","zip","number","quarter","city"]
estore1 = estore["data"]
i = 0
estore2 = {}
estore2['estore'] = []
while i < len(estore1) :
    liste2 = estore1[i]
    liste2.remove(liste2[0])
    liste2.remove(liste2[0])
    liste2.remove(liste2[0])
    liste2.remove(liste2[0])
    liste2.remove(liste2[0])
    liste2.remove(liste2[0])
    liste2.remove(liste2[1])
    liste2.remove(liste2[2])
    liste2.remove(liste2[3])
    liste2.remove(liste2[5])
    liste2.remove(liste2[7])
    liste2.remove(liste2[7])
    liste2.remove(liste2[7])
    estore2['estore'].append({ 
        column2[0] : str(liste2[0]),  
        column2[1] : str(liste2[1]),
        column2[2] : str(liste2[2]),
        column2[3] : str(liste2[3]),
        column2[4] : str(liste2[4]),
        column2[5] : str(liste2[5]),
        column2[6] : str(liste2[6])
})
    i+=1 


with open('$HOME/NoSQLTheoVleeschouwers/estore_clean.json', 'w') as f2:
    json.dump(estore2['estore'],f2)