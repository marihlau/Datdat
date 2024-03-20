import sqlite3

db_file = "TrondelagTeater.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

def findAvalibleSeats(stykkeNavn, dato, antallSeter, mobilnr):
    cursor.execute('''SELECT stykkeID FROM teaterStykke WHERE navn = ?''', (stykkeNavn,))
    resultat = cursor.fetchone()
    
    if resultat:
        stykkeID = resultat[0]     
        print("dato:", dato)
        print("stykkeid:", stykkeID)
    else:
        print("Fant ikke stykkenavn i database") 

    cursor.execute('''SELECT salID FROM teaterStykke WHERE navn = ?''', (stykkeNavn,))
    resultat = cursor.fetchone()
    if resultat:
        salID = resultat[0]
        print(salID)
    else:
        print("Fant ikke salID")

    cursor.execute('''SELECT forestillingID FROM forestilling WHERE dato = ? AND stykkeID = ?''', (dato, stykkeID,))
    resultat = cursor.fetchone()
    if resultat:
        forestillingID = resultat[0]
        print("forestillingID:", forestillingID)
    else:
        print("Ingen forestilling den dagen")

    query = '''SELECT p.omraade, p.radNR, COUNT(p.plassID) as ledig_seter 
    FROM plass p 
    LEFT JOIN billett b ON b.forestillingID = ? AND p.plassID = b.plassID
    WHERE salID = ? AND b.plassID IS NULL
    GROUP BY p.omraade, p.radNR
    HAVING COUNT(p.plassID) >= ?'''

    cursor.execute(query, (forestillingID, salID, antallSeter,))

    raderMedLedigeSeter = cursor.fetchall()

    

    cursor.execute('''SELECT gruppeID FROM kundeProfil WHERE mobilNR = ? ''', (mobilnr,))
    resultat = cursor.fetchone()

    if resultat:
        gruppeID = resultat[0]
    else:
        print("GruppeID ikke funnet")


    if antallSeter >= 10 and gruppeID == 1:
        pris = 320 * antallSeter
    elif antallSeter >= 10 and gruppeID == 2:
        pris = 270 * antallSeter
    else:
        cursor.execute('''SELECT pris FROM kanSe WHERE gruppeID = ? ''', (gruppeID,))
        resultat = cursor.fetchone()

        if resultat:
            billetpris = resultat[0]
        else:
            print("Fant ikke pris")
        pris = billetpris * antallSeter

    conn.close()

    if raderMedLedigeSeter:
        print(f'Rader med {antallSeter} eller flere ledige seter for {stykkeNavn} med en pris på {pris}kr')
        for rad in raderMedLedigeSeter:
            print(f'Rad {rad[1]} i {rad[0]} har {rad[2]} ledige seter')
    else:
        print(f'Fant ingen rader med {antallSeter} ledige seter for {stykkeNavn} på datoen {dato}')
    
    #if forestillingID:
        #cursor.execute('''SELECT plassID FROM billett WHERE forestillingID = ?''', (forestillingID[0],))
        #plassid = cursor.fetchall()
        #print("plassid:", plassid)
        #print("Number of available seats:", len(plassid))
    #else:
        #print("No forestillingID found for the given criteria.")

findAvalibleSeats("Størst av alt er kjærligheten", 3.2, 9, 99999999) #skal returnere 2 seter

conn.close()