import pandas as pd


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)


#Question 8 -> nutzen der loc() funktion, um auf alle die Einträge zu zugreifen, bei denen der Preis leer ist und entsprechend kein Auto gekauft wurde und die Personen 
# nur besucher in dem Showroom waren. Auf diese Menge von Einträgen wird der Filter 'Alter' angewandt und der mean() gezogen.
q8 =  data.loc[data['Preis'].isna(), 'Alter'].mean()
print(q8)