import pandas as pd

#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Zugriff auf nur die Einträge, die als männlich gekennzeichnet sind und keinen eintrag bei Preis haben über die loc() funktion 
#Als bedingung wird Geschlecht gleich Männlich überreicht und dass Preis leer ist. Auf die ausgabe von loc() wird der Mean() angewnadt 
q9 = data.loc[(data['Geschlecht'] == 1.0) & (~data['Preis'].isna()), 'Alter'].mean()
print(q9)