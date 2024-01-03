import pandas as pd
from scipy.stats import pearsonr


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Question 11 -> fitern der Data-Datei nach nur den einträgen, die einen Preis eingetragen haben, um nur die Kunden in der Datei zu haben 
 
df_filtered = data.dropna(subset=['Preis'])

#Errechnung der Pearson Korrellation zwischen den Variablen: Preis, Einkommen, zeit und Alter (Nur für die Kunden)
q11_1 = pearsonr(df_filtered['Alter'], df_filtered['Preis'])
q11_2 = pearsonr(df_filtered['Alter'], df_filtered['Einkommen'])
q11_3 = pearsonr(df_filtered['Alter'], df_filtered['Zeit'])
q11_4 = pearsonr(df_filtered['Einkommen'], df_filtered['Zeit'])
q11_5 = pearsonr(df_filtered['Einkommen'], df_filtered['Preis'])
q11_6 = pearsonr(df_filtered['Preis'], df_filtered['Zeit'])
print(...)