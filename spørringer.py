import sqlite3

db_file = "test.db"  

conn = sqlite3.connect(db_file)
cursor = conn.cursor()


cursor.execute(''' 
               SELECT DISTINCT teaterStykke.navn, spillerRolle.navn, ansatt.navn
               FROM (teaterStykke JOIN spillerRolle ON spillerRolle.stykkeID = teaterstykke.stykkeID) 
               JOIN ansatt ON ansatt.ansattID = spillerRolle.ansattID
               ''')

cursor.execute('''
               SELECT teaterstykke.navn, forestilling.dato , COUNT (billet.billetID) AS antallBiletter
               FROM (forestilling JOIN teaterstykke ON forestilling.stykkeID=teaterstykke.stykkeID)
               JOIN billet ON billet.forestillingID=forestilling.forestillingID
               GROUP BY teaterstykke.navn
               ORDER BY antallBiletter DESC
               ''')

conn.commit()
conn.close()

