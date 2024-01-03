import pandas as pd



#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Question 1 -> verwendung der count() funktion aus pandas zur Zählung der Einträge in der Spalte "Preis". 
# Preis als spalte daher gewählt, da nur bei den Kunden ein Preis eingetragen ist, die auch ein Auto gekauft haben. 
# Diejenigen, die lediglich interessiert waren sind ohne Preis erfasst.

q1 = data['Preis'].count()
print(q1)