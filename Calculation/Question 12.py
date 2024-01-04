import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, norm
import statsmodels.api as sm


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)


#Question 12 -> Erstellung eines Histogrammes der Verteilung der Variable Zeit mit der Funktion .hist() von Matplotlib.
# Ebenfalls konkretisierung der Attribute der Darstellung wie Größe und Anzahl der Bins sowie beschriftung der Achsen  
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

