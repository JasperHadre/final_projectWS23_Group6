import pandas as pd



#import df_final.csv 
data = pd.read_csv("df_final.csv", index_col=0)

#Question 3 -> verwendung der sum() funktion von pandas, um den gesamtumsatz herauszufinden: 

q3 = data['Preis'].sum()
print(q3)