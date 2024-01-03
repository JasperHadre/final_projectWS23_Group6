import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Filtern der Data-Datei, um nur die Einträge zu erhalten, bei denen ein Preis eingetragen ist (nur die Kuden)
df_filtered = data.dropna(subset=['Preis'])

#Question 13 -> filtern des DF nach den Personen, bei denen der Preis höher ist, als das Einkommen, danach verwendung der sum() funktion, um die Anzahl zu erfahren
q_13 = (df_filtered['Einkommen'] > df_filtered['Preis']).sum()
print(q_13)
