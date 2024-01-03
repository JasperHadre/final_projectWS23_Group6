import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
import statsmodels.api as sm

# Importiere df_final.csv
data = pd.read_csv("df_final.csv", index_col=0)

# Frage 14
df_filtered2 = data.dropna()

# Abhängige Variable definieren: Preis
y = df_filtered2['Preis']

# Unabhängige Variablen definieren:
X = df_filtered2[['Einkommen', 'Alter', 'Geschlecht']]

# Standardisieren der unabhängigen Variablenn (für standardisierte koeffizienten)
X_scaled = scale(X)

# Hinzufügen einer Konstanten als Intercept in der Regression
X_scaled = sm.add_constant(X_scaled)

# Modell aufrufen
model = sm.OLS(y, X_scaled)

# Modell ausrechnen
results = model.fit()

# Ausgabe der standardisierten Regressionskoeffizienten
#Für einkommen:
print(results.params['x1'])
#Für Alter:
print(results.params['x2'])
#Für Geschlecht
print(results.params['x3'])
print("Das Einkommen beeinflusst den Kaufpreis am meisten!")