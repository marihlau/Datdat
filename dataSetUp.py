import sqlite3

db_file = "TrondelagTeater.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

kundegrupper = ["ordinær", "honnør", "student", "barn"]

def setteOppKundegrupper():
    for gruppe in kundegrupper:
        cursor.execute('''INSERT INTO kundeGruppe VALUES (NULL, ?)''', (gruppe,))
        conn.commit()

setteOppKundegrupper()
conn.commit()

cursor.execute('''SELECT DISTINCT gruppeID FROM kundeGruppe WHERE gruppenavn = ?''', ("ordinær",))
resultat =  cursor.fetchone()
if resultat:
    ordinaer = resultat[0]

cursor.execute('''insert into kundeprofil (kundeid, navn, mobilnr, adresse, gruppeid) values (NULL, "Standardbruker", "99999999", "Hovedscenen", ?)''', (ordinaer,))
kundeid = cursor.lastrowid
conn.commit()




conn.close()