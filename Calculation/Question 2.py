import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Question 2 -> herausfinden des höchsten, niedrigsten und durchschnittlichen Preises der Autos mithilfe der Max(); min() und mean() funktionen von Pandas. 
q2_1 = data['Preis'].max()
q2_2 = data['Preis'].min()
q2_3 = data['Preis'].mean()
print(q2_1)
print(q2_2)
print(q2_3)