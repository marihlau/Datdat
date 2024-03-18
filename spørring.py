import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()


cursor.execute(''' 
               SELECT DISTINCT teaterStykke.navn, spillerRolle.navn, skuespiller.navn
               FROM (teaterStykke JOIN spillerRolle ON spillerRolle.stykkeID = teaterstykke.stykkeID) 
               JOIN skuespiler ON skuespiller.ansattID = spillerRolle.ansattID
               ''')

cursor.execute('''
               SELECT teaterstykke.navn, DISTINCT (forestilling.dato) , COUNT (billet)
               FROM (forestilling JOIN teaterstykke ON forestilling.stykkeID=teaterstykke.stykkeID)
               JOIN billet ON billet.foretillingID=forestilling.forestillingID
               GROUP BY (teaterstykke.navn)
               ORDER BY(COUNT billet) DESC
               ''')

