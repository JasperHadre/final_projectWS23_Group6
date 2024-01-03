from Question17 import results

intercept = results.params['const']  # Intercept
coefficient_einkommen = results.params['Einkommen']  # Koeffizient für 'Einkommen'
coefficient_alter = results.params['Alter']  # Koeffizient für 'Alter'
coefficient_geschlecht = results.params['Geschlecht']  # Koeffizient für 'Alter'
coefficient_zeit = results.params['Zeit']  # Koeffizient für 'Alter'

#Question 18 -> Errechnung der Wahrscheinlichkeiten für die beiden gegebenen Fälle
case3 = intercept + (coefficient_alter*32)+ (coefficient_einkommen*30000)+(coefficient_geschlecht*1)+(coefficient_zeit*30)
print(case3)

case4 = intercept + (coefficient_alter*51)+ (coefficient_einkommen*54000)+(coefficient_geschlecht*1)+(coefficient_zeit*45)
print(case4)