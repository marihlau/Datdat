import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

def findAvalibleSeats(stykkeNavn, dato, antallSeter):
    stykkeid = cursor.execute('''SELECT stykkeID FROM teaterStykke WHERE navn = ?''' ,(stykkeNavn,))
    forestillingID = cursor.execute('''SELECT forestillingID FROM forestilling WHERE dato = ? AND stykkeID = ?''', (dato, stykkeid,))
    plassid = cursor.execute('''SELECT plassID FROM billett WHERE forestillingID = ?''', (forestillingID,))

   