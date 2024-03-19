import sqlite3

db_file = "test.db"  

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute(''' INSERT INTO teaterStykke 
               VALUES(1, "Kongsemnene", "Ibsen", 1)
               ''')
cursor.execute(''' INSERT INTO spillerRolle
               VALUES (1, 1, "kongen")
               ''')

cursor.execute(''' INSERT INTO ansatt
               VALUES (1, "ola","ol9715469@gmail.com", "deltid" )
               ''')

cursor.execute(''' INSERT INTO forestilling
               VALUES (1, 18, 19, 1)
               ''')

cursor.execute(''' INSERT INTO billet
               VALUES (1, 1, 1, 1)
               ''')



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
               SELECT teaterstykke.navn, forestilling.dato , COUNT (billet.billetID) AS antallBiletter
               FROM (forestilling JOIN teaterstykke ON forestilling.stykkeID=teaterstykke.stykkeID)
               JOIN billet ON billet.forestillingID=forestilling.forestillingID
               GROUP BY teaterstykke.navn
               ORDER BY antallBiletter DESC
               ''')

result = cursor.fetchall()
for row in result:
    print (row)
    print ("\n")

conn.commit()
conn.close()
