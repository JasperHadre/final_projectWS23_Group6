import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Question 14

#Einträge löschen, die eine NA beinhalten. Diese stören die OLS Funktion und führen zu error; mithilfe von dropna()
df_filtered2 = data.dropna()

# Abhängige Variable definieren: 
y = df_filtered2['Preis']

# Unabhängige Variablen Definieren:
X = df_filtered2[['Einkommen', 'Alter', 'Geschlecht']]

# Hinzufügen des Intercept für die Regression
X = sm.add_constant(X)

# Modell aufrufen (OLS als Rechenweise)
model = sm.OLS(y, X)

# Modell fitten lassen
results = model.fit()

# Ausgabe der Regressionsergebnisse
print(results.summary())