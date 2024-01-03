import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Question 17 
#Hinzufügen einer weiteren Spalte, 'Kauf getätigt' als Dummy Variable. Diese ist 1 wenn ein Auto gekauft wurde und 0 wenn nicht. 
data['Kauf_getaetigt'] = data['Preis'].notna().astype(int)

#Ersetzen der NA Einträge in der Spalte Preis mit Null, da sonst alle Besucher im nächsten Schritt gelöscht werden
data['Preis'] = data['Preis'].fillna(0)

#Löschen aller einträge, die NA enthalten, da diese die Funktion sm.logit() stören und einen error hervorrufen
df_filtered3 = data.dropna()

# Unabhängige Variablen (X) definieren
X = df_filtered3[['Einkommen', 'Zeit','Geschlecht','Alter']]

# Hinzufügen einer Konstanten für den Intercept in der Regression
X = sm.add_constant(X)

# Abhängige Variable definieren (binär)
y = df_filtered3['Kauf_getaetigt']

# Modell aufrufen (logistisch)
model = sm.Logit(y, X)

# Modell fitten
results = model.fit()

# Ausgabe der logistischen Regressionskoeffizienten
print(results.summary())
