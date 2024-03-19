import sqlite3

db_file = "test.db"  

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute(''' INSERT INTO teaterStykke 
               VALUES(9, "Kongsemnene", "Ibsen", 9)
               ''')
cursor.execute(''' INSERT INTO teaterStykke 
               VALUES(7, "Størst av alt er kjærligheten", "Petersen", 7)
               ''')
cursor.execute(''' INSERT INTO spillerRolle
               VALUES (9, 9, "kongen")
               ''')

cursor.execute(''' INSERT INTO ansatt
               VALUES (9, "ola","ole@gmail.com", "deltid" )
               ''')

cursor.execute(''' INSERT INTO forestilling
               VALUES (9, 18, 19, 9)
               ''')
cursor.execute(''' INSERT INTO forestilling
               VALUES (7, 18, 19, 7)
               ''')

cursor.execute(''' INSERT INTO billett
               VALUES (9, 9, 9, 9)
               ''')
cursor.execute(''' INSERT INTO billett
               VALUES (7, 9, 9, 9)
               ''')
cursor.execute(''' INSERT INTO billett
               VALUES (8, 9, 7, 9)
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
               SELECT teaterstykke.navn, forestilling.dato , COUNT (billett.billettID) AS antallBiletter
               FROM (forestilling JOIN teaterstykke ON forestilling.stykkeID=teaterstykke.stykkeID)
               JOIN billett ON billett.forestillingID=forestilling.forestillingID
               GROUP BY teaterstykke.navn, forestilling.dato
               ORDER BY antallBiletter DESC
               ''')

result = cursor.fetchall()
for row in result:
    print (row)
    print ("\n")

conn.commit()
conn.close()

