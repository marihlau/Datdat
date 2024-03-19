import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

def findAvalibleSeats(stykkeNavn, dato, antallSeter):
    cursor.execute('''SELECT stykkeID FROM teaterStykke WHERE navn = ?''', (stykkeNavn,))
    stykkeid = cursor.lastrowid     
    print("dato:", dato)
    print("stykkeid:", stykkeid)

    cursor.execute('''SELECT forestillingID FROM forestilling WHERE dato = ? AND stykkeID = ?''', (dato, stykkeid,))
    forestillingID = cursor.fetchone()
    print("forestillingID:", forestillingID)
    
    if forestillingID:
        cursor.execute('''SELECT plassID FROM billett WHERE forestillingID = ?''', (forestillingID[0],))
        plassid = cursor.fetchall()
        print("plassid:", plassid)
        print("Number of available seats:", len(plassid))
    else:
        print("No forestillingID found for the given criteria.")

findAvalibleSeats("Kongsemnene", 19, 2) #skal returnere 2 seter

conn.close()