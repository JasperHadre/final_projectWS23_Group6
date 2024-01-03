import pandas as pd



#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Question 4 -> verwendung der value_counts() funktion aus pandas, welche zählt, wie oft verschiedene Werte in einem DF vorkommen. 
# Die Funktion gruppiert dabei automatisch die jeweiligen Werte. 

q4 = data['Niederlassung'].value_counts()
print(q4)