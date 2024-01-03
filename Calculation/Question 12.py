import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import statsmodels.api as sm


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)


#Question 12 -> Erstellung eines Histogrammes der Verteilung der Variable Zeit mit der Funktion .hist() von Matplotlib.
# Ebenfalls konkretisierung der Attribute der Darstellung wie Größe und Anzahl der Bins sowie beschriftung der Achsen  
plt.figure(figsize=(10, 6))
data['Zeit'].hist(bins=50, color='skyblue', edgecolor='black')
plt.title('Verteilung der Zeit')
plt.xlabel('Zeit')
plt.ylabel('Anzahl der Einträge')
plt.show()