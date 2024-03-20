import sqlite3

db_file = "TrondelagTeater.db"  

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute(''' 
               SELECT DISTINCT teaterStykke.navn, spillerRolle.navn, ansatt.navn
               FROM (teaterStykke JOIN spillerRolle ON spillerRolle.stykkeID = teaterstykke.stykkeID) 
               JOIN ansatt ON ansatt.ansattID = spillerRolle.ansattID
               ''')

result = cursor.fetchall()
for row in result:
    print (row)
    print ("\n")

#Litt usikker på om denne gir riktig svar
cursor.execute('''
               SELECT teaterstykke.navn, forestilling.dato , COUNT (billett.billettID) AS antallBiletter
               FROM (forestilling JOIN teaterstykke ON forestilling.stykkeID=teaterstykke.stykkeID)
               JOIN billett ON billett.forestillingID=forestilling.forestillingID
               GROUP BY teaterstykke.navn
               ORDER BY antallBiletter DESC
               ''')

result = cursor.fetchall()
for row in result:
    print (row)
    print ("\n")

conn.commit()
conn.close()

