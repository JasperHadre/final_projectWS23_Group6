#Importieren der Regressionskoeffizienten aus Q14
from Question14 import results

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
import statsmodels.api as sm


#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

intercept = results.params['const']  # Intercept aus results aufrufen 
coefficient_einkommen = results.params['Einkommen']  # Koeffizient für 'Einkommen' aus results aufrufen
coefficient_alter = results.params['Alter']  # Koeffizient für 'Alter' aus results aufrufen
coefficient_geschlecht = results.params['Geschlecht']  # Koeffizient für 'Alter' aus results aufrufen
#Fall 1: berechnung der Werte anhand der Koeffizienten:
case1 = intercept + (coefficient_einkommen * 30000)+ (coefficient_alter * 32) + (coefficient_geschlecht * 1)
print(case1)
#Fall 2 
case2 = intercept + (coefficient_einkommen * 54000)+ (coefficient_alter * 51) + (coefficient_geschlecht * 1)
print(case2)