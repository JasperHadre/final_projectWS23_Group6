import pandas as pd


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Question 5 -> Verwendung der Funktion groupby() iVm mean() um den durchschnittlichen Umsatz pro Niederlassung heraus zu finden. 
# Funtiion groupby nimmt ein Argument, nachdem Gruppuiert wird und wendet es auf die jeweilige spalte an. Pro Gruppe wird dann der Durchschnitt gebildet.

q5 = data.groupby('Niederlassung')['Preis'].mean()
print(q5)