import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, norm
import statsmodels.api as sm
from sklearn.preprocessing import scale


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

#Question 10 
q10 = data.dropna(subset=['Preis'])['Einkommen'].mean()
print(q10)

#Question 11
df_filtered = data.dropna(subset=['Preis'])

q11_1 = pearsonr(df_filtered['Alter'], df_filtered['Preis'])
q11_2 = pearsonr(df_filtered['Alter'], df_filtered['Einkommen'])
q11_3 = pearsonr(df_filtered['Alter'], df_filtered['Zeit'])
q11_4 = pearsonr(df_filtered['Einkommen'], df_filtered['Zeit'])
q11_5 = pearsonr(df_filtered['Einkommen'], df_filtered['Preis'])
q11_6 = pearsonr(df_filtered['Preis'], df_filtered['Zeit'])
print(q11_6)


#Question 12
plt.figure(figsize=(10, 6))
counts, bins, _ = plt.hist(data['Zeit'], bins=100, color='skyblue', edgecolor='black', density=True, label='Histogram')

# Berechne Mittelpunkte der Bins
bin_centers = 0.5 * (bins[:-1] + bins[1:])

# Füge Normalverteilungslinie hinzu (angepasste Amplitude)
mean, std = data['Zeit'].mean(), data['Zeit'].std()
p = norm.pdf(bin_centers, mean, std) * (np.max(counts) / np.max(norm.pdf(bin_centers, mean, std)))  # Amplitude anpassen
plt.plot(bin_centers, p, 'k', linewidth=2, label='Normalverteilung')

# Beschriftungen und Titel
plt.title('Histogramm und Normalverteilung der Zeit')
plt.xlabel('Zeit')
plt.ylabel('Dichte')
plt.legend()

# Zeige das Diagramm
plt.show()

# seems to be normally distributed 

#Question 13
q_13 = (df_filtered['Einkommen'] > df_filtered['Preis']).sum()
print(q_13)

#Question 14
df_filtered2 = data.dropna()
# Abhängige Variable (y): Preis
y = df_filtered2['Preis']

# Unabhängige Variable (X): Hier wähle ich 'Einkommen' als Beispiel, du kannst andere Variablen wählen
X = df_filtered2[['Einkommen', 'Alter', 'Geschlecht']]

# Hinzufügen einer Konstanten für den Intercept in der Regression
X = sm.add_constant(X)

# Modell erstellen
model = sm.OLS(y, X)

# Modell anpassen
results = model.fit()

# Ausgabe der Regressionskoeffizienten
print(results.summary())

#Question 15
intercept = results.params['const']  # Intercept
coefficient_einkommen = results.params['Einkommen']  # Koeffizient für 'Einkommen'
coefficient_alter = results.params['Alter']  # Koeffizient für 'Alter'
coefficient_geschlecht = results.params['Geschlecht']  # Koeffizient für 'Alter'
#Fall 1:
case1 = intercept + (coefficient_einkommen * 30000)+ (coefficient_alter * 32) + (coefficient_geschlecht * 1)
print(case1)
#Fall 2 
case2 = intercept + (coefficient_einkommen * 54000)+ (coefficient_alter * 51) + (coefficient_geschlecht * 1)
print(case2)

#Question 16 
# Das Alter beeinflusst den Kaufpreis am meiste. Jedoch scheinen alter und Einkommen multicollinear zu einander verteilt zu sein, dem entsprechend keine verlässliche Aussage

# Abhängige Variable definieren: Preis
y3 = df_filtered2['Preis']

# Unabhängige Variablen definieren:
X3 = df_filtered2[['Einkommen', 'Alter', 'Geschlecht']]

# Standardisieren der unabhängigen Variablenn (für standardisierte koeffizienten)
X_scaled = scale(X3)

# Hinzufügen einer Konstanten als Intercept in der Regression
X_scaled = sm.add_constant(X_scaled)

# Modell aufrufen
model3 = sm.OLS(y3, X_scaled)

# Modell ausrechnen
results3 = model3.fit()

# Ausgabe der standardisierten Regressionskoeffizienten
#Für einkommen:
print(results3.params['x1'])
#Für Alter:
print(results3.params['x2'])
#Für Geschlecht
print(results3.params['x3'])
print("Das Einkommen beeinflusst den Kaufpreis am meisten!")


#Question 17 
#Hinzufügen einer weiteren Spalte, 'Kauf getätigt' als Dummy Variable. Diese ist 1 wenn ein Auto gekauft wurde und 0 wenn nicht. 
data['Kauf_getaetigt'] = data['Preis'].notna().astype(int)

#Ersetzen der NA Einträge in der Spalte Preis mit Null, da sonst alle Besucher im nächsten Schritt gelöscht werden
data['Preis'] = data['Preis'].fillna(0)

#Löschen aller einträge, die NA enthalten, da diese die Funktion sm.logit() stören und einen error hervorrufen
df_filtered3 = data.dropna()

# Unabhängige Variablen (X) definieren
X2 = df_filtered3[['Einkommen', 'Zeit','Geschlecht','Alter']]

# Hinzufügen einer Konstanten für den Intercept in der Regression
X2 = sm.add_constant(X2)

# Abhängige Variable definieren (binär)
y2 = df_filtered3['Kauf_getaetigt']

# Modell aufrufen (logistisch)
model2 = sm.Logit(y2, X2)

# Modell fitten
results2 = model2.fit()

# Ausgabe der logistischen Regressionskoeffizienten
print(results2.summary())


intercept2 = results2.params['const']  # Intercept
coefficient_einkommen2 = results2.params['Einkommen']  # Koeffizient für 'Einkommen'
coefficient_alter2 = results2.params['Alter']  # Koeffizient für 'Alter'
coefficient_geschlecht2 = results2.params['Geschlecht']  # Koeffizient für 'Alter'
coefficient_zeit2 = results2.params['Zeit']  # Koeffizient für 'Alter'

#Question 18 
case3 = intercept2 + (coefficient_alter2*32)+ (coefficient_einkommen2*30000)+(coefficient_geschlecht2*1)+(coefficient_zeit2*30)
print(case3)
case4 = intercept2 + (coefficient_alter2*51)+ (coefficient_einkommen2*54000)+(coefficient_geschlecht2*1)+(coefficient_zeit2*45)
print(case4)