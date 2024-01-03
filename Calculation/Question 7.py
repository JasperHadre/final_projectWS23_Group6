import pandas as pd


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)



#Question 7 -> verwendung der dropna() funktion, um alle leeren Einträge der Spalte "Preis" zu löschen, um nur die Kunden zu erhalten und nicht die Besucher
# danach wenden wir die gefilterte Preis Spalte zusammen mit der Mean() funktion auf die "Alter" Spalte an, um das durchschnittliche Alter der Kunden zu erhalten.
q7 = data.dropna(subset=['Preis'])['Alter'].mean()
print(q7)