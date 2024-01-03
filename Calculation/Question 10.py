import pandas as pd


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)


#Question 10 -> filtern der Einträge nach nur denen, die einen Preis eingteragen haben, um nur die Kunden zu erhalten (dropna())
# anwenden der mean() Funktion auf die Spalte "Einkommen" der Auswahl 

q10 = data.dropna(subset=['Preis'])['Einkommen'].mean()
print(q10)
