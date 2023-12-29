import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels as st


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Question 1
q1 = data['Preis'].count()
print(q1)

#Question 2
q2_1 = data['Preis'].max()
q2_2 = data['Preis'].min()
q2_3 = data['Preis'].mean()
print(q2_1)
print(q2_2)
print(q2_3)

#Question 3
q3 = data['Preis'].sum()
print(q3)

#Question 4
q4 = data['Niederlassung'].value_counts()
print(q4)

#Question 5
q5 = data.groupby('Niederlassung')['Preis'].mean()
print(q5)

#Question 6
q6 = data.groupby('Geschlecht')['Preis'].count()
if q6[1.0] > q6[0.0]:
    print("Mehr Männer haben Autos gekauft.")
elif q6[0.0] <q6[1.0]:
    print("Mehr Frauen haben Autos gekauft.")
else:
    print("Es haben gleich viele Frauen und Männer Autos gekauft.")

#Question 7 
q7 = data.dropna(subset=['Preis'])['Alter'].mean()
print(q7)

#Question 8
q8 =  data.loc[data['Preis'].isna(), 'Alter'].mean()
print(q8)

#Question 9 
q9 = data.loc[(data['Geschlecht'] == 1.0) & (~data['Preis'].isna()), 'Alter'].mean()
print(q9)

#Question 9 
q9 = data.dropna(subset=['Preis'])['Einkommen'].mean()
print(q9)

#Question 10 
q10 = weightstats.pearsonr(df_filtered['Alter'], df_filtered['Preis'])
