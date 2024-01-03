import pandas as pd


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)




#Question 6 -> um herauszufinden, ob Männer oder Frauen mehr Autos gekauft haben gruppieren wir die 'Preis' Spalte (als indikatoin ob ein Verkauf stattgefunden hat) nach dem Geschlecht 
#danach verwendung der count() funkition, um herauszufinden, wie viele Autos pro Geschlecht verkauft wurden
q6 = data.groupby('Geschlecht')['Preis'].count()

#Ausgabe der Antwort, je nachdem weldhes Geschlecht höher ist. Vergleich in einer If-funktion, welche das Ergebnis aufruft.
if q6[1.0] > q6[0.0]:
    print("Mehr Männer haben Autos gekauft.")
elif q6[0.0] <q6[1.0]:
    print("Mehr Frauen haben Autos gekauft.")
else:
    print("Es haben gleich viele Frauen und Männer Autos gekauft.")
#(print(q6[1.0]))