# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Defining the Panda dataframe, (using "delimiter" because the csv file imports the values with a semicolon instead of a comma)
kunden = pd.read_csv("kunden.csv",delimiter=";",index_col=5)
besucher = pd.read_csv("besucher.csv",delimiter=";",index_col=4)

#Creating a geo.csv file from geo.txt 
geo_txt = pd.read_csv("geo.txt", delimiter= "\s+")
geo_txt.to_csv("geo.csv", index=False)
geo = pd.read_csv("geo.csv", index_col=0)

#Removing geo.txt 
import os
os.remove("geo.txt")

#Converting the , to . in the "besucher" dataframe
besucher = besucher.replace(",",".",regex=True)

#Cleaning out geo: 
    # 1. checking all unique values to see if there are inconsistencies
    
print(geo["Niederlassung"].unique())

    # 2. replacing the values so each "Bundesland" only has one value associated to it
    
geo = geo.replace("NRW","Nordrhein-Westfalen",regex=True)
geo = geo.replace("BERLIN","Berlin",regex=True)
geo = geo.replace("Berlin-Charlottenburg","Berlin",regex=True)
geo = geo.replace("Berlin-Mitte","Berlin",regex=True)

    # 3. checking all unique values again to make sure all inconsistencies are fixed

print(geo["Niederlassung"].unique())

#Cleaning out kunden:
    #1. checking wether there are extreme values with  scatter plots:

plt.scatter(range(len(kunden)),kunden["Alter"])
plt.show()
plt.clf()

plt.scatter(range(len(kunden)), np.log(kunden["Einkommen"]))
plt.show()
plt.clf()

plt.scatter(range(len(kunden)),kunden["Preis"])
plt.show()
plt.clf()

plt.scatter(range(len(kunden)),kunden["Geschlecht"])
plt.show()
plt.clf()

plt.scatter(range(len(kunden)),kunden["Zeit"])
plt.show()
plt.clf()

    #2. We have found 2 outliers in the column "Alter" and 3 outliers in the column "Einkommen", now we will remove the outliers:
        
kunden = kunden[(kunden["Alter"] < 80 ) & (kunden["Einkommen"] > 0 ) & (kunden["Einkommen"] < 1000000000)]

#Cleaning out besucher
    #1. checking wether there are extreme values with  scatter plots:

plt.scatter(range(len(besucher)),besucher["Alter"])
plt.show()
plt.clf()

plt.scatter(range(len(besucher)), np.log(pd.to_numeric(besucher["Einkommen"])))
plt.show()
plt.clf()

plt.scatter(range(len(besucher)),besucher["Geschlecht"])
plt.show()
plt.clf()

plt.scatter(range(len(besucher)),besucher["Zeit"])
plt.show()
plt.clf()

    #2. Did not find any outliers. All data is cleaned  


#Printing the 3 data frames
print(geo)
print(kunden)
print(besucher)