import sqlite3
kundegrupper = ["ordinær", "honnør", "student", "barn"]
db_file = "TrondelagTeater.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('''INSERT INTO sal VALUES (NULL, "Gamle scene", 332)''')
conn.commit()

sal_id = cursor.lastrowid

cursor.execute('''INSERT INTO teaterStykke VALUES (NULL, "Størst av alt er kjærligheten", "Petersen", ?)''', (sal_id,))
conn.commit()

stykke_id = cursor.lastrowid

cursor.execute('''INSERT INTO akt VALUES (?, 1, 1) ''', (stykke_id,))
conn.commit()


def settInnForestilling (start_tid, dato):
    cursor.execute('''INSERT INTO forestilling VALUES (NULL, ?, ?, ?) ''', (start_tid, dato, stykke_id))

settInnForestilling(1830, 3.2)
settInnForestilling(1830, 6.2)
settInnForestilling(1830, 7.2)
settInnForestilling(1830, 12.2)
settInnForestilling(1830, 13.2)
settInnForestilling(1830, 14.2)
forestillingID = cursor.lastrowid

conn.commit()

def  settOppkanSeStorstAvAlt():

    cursor.execute('''SELECT stykkeID FROM teaterStykke WHERE navn = ?''', ("Størst av alt er kjærligheten",))
    SjekkstykkeID = cursor.fetchone()
    if SjekkstykkeID:
        stykkeID = SjekkstykkeID[0]
    else:
        print("Fant ikke stykkeID")

    for gruppe in kundegrupper:
        
        cursor.execute('''SELECT gruppeID FROM kundeGruppe WHERE gruppenavn = ?''', (gruppe,))
        sjekkgruppeID = cursor.fetchone()
        if sjekkgruppeID:
            gruppeID = sjekkgruppeID[0]
        else:
            print("Fant ikke gruppeID")
        if gruppe == "ordinær":
            cursor.execute('''INSERT INTO kanSe VALUES (?, ?, 350)''', (gruppeID, stykkeID,))
        elif gruppe == "honnør":
            cursor.execute('''INSERT INTO kanSe VALUES (?, ?, 300)''', (gruppeID, stykkeID,))
        elif gruppe == "student":
            cursor.execute('''INSERT INTO kanSe VALUES (?, ?, 220)''', (gruppeID, stykkeID,))
        elif gruppe == "barn":
            cursor.execute('''INSERT INTO kanSe VALUES (?, ?, 220)''', (gruppeID, stykkeID,))

settOppkanSeStorstAvAlt()
conn.commit()

#Henter ut info om standarbruker:
cursor.execute('''SELECT kundeID FROM kundeProfil WHERE navn = ?''', ("Standardbruker",))  
sjekkStandardbruker = cursor.fetchone()
if sjekkStandardbruker:
    kundeid = sjekkStandardbruker[0]
#Henter ut forestillingID for en abitrær forestilling av Størst av alt er kjærligheten
cursor.execute('''SELECT forestillingID FROM forestilling WHERE stykkeID = ?''', (stykke_id,))
sjekForestilling = cursor.fetchone()
if sjekForestilling:
    forestillingID = sjekForestilling[0]

filePath = 'gamle-scene.txt'

cursor.execute('''insert into kundegruppe (gruppeid, gruppenavn) values (NULL, "Standardbruker")''')
gruppeid = cursor.lastrowid
cursor.execute('''insert into kundeprofil (kundeid, navn, mobilnr, adresse, gruppeid) values (NULL, "Standardbruker", "99999991", "Hovedscenen", ?)''', (gruppeid,))
kundeid = cursor.lastrowid
conn.commit()

def setteStolerGamleScene (filePath):
    #Åpner filen og leser filen 
    with open(filePath, 'r') as file:
        lines = file.readlines()

    område = None
    radNr = 0
    seteNr = 0 

    for line in lines:
        # Ser om vi er i galleri, balkong eller parkett området
        if 'Galleri' in line:
            område = 'Galleri'
            radNr = 4
            seteNr = 0
        elif 'Balkong' in line:
            område = 'Balkong'
            radNr = 5
            seteNr = 0
        elif 'Parkett' in line:
            område = 'Parkett'
            radNr = 11
            seteNr = 0
        
        else:
            if område == 'Galleri':
                radNr -= 1
                seteNr = 0
                for char in line.strip():
                    if char == '0':
                        seteNr +=1
                        cursor.execute('''INSERT INTO plass VALUES (NULL, ?, ?, ?, ?) ''', (radNr, seteNr, område, sal_id,))
                        conn.commit()
                    elif char == '1':
                        seteNr +=1
                        cursor.execute('''INSERT INTO plass VALUES (NULL, ?, ?, ?, ?) ''', (radNr, seteNr, område, sal_id,))
                        plassid = cursor.lastrowid
                        conn.commit()
                        cursor.execute('''INSERT INTO billettKjop VALUES (NULL, ?, 14.38, 19.03) ''', (kundeid,))
                        kjopsid = cursor.lastrowid
                        conn.commit()
                        cursor.execute('''INSERT INTO billett VALUES (NULL, ?, ?, ?) ''', (kjopsid, forestillingID ,plassid,))
                        conn.commit()
            elif område == 'Balkong':
                radNr -=1
                seteNr = 0
                for char in line.strip():
                    if char == '0':
                        seteNr +=1
                        cursor.execute('''INSERT INTO plass VALUES (NULL, ?, ?, ?, ?) ''', (radNr, seteNr, område, sal_id,))  
                        conn.commit()
                    elif char == '1':
                        seteNr +=1
                        cursor.execute('''INSERT INTO plass VALUES (NULL, ?, ?, ?, ?) ''', (radNr, seteNr, område, sal_id,))
                        plassid = cursor.lastrowid
                        conn.commit()
                        cursor.execute(''' INSERT INTO billettKjop VALUES (NULL, ?, 14.38, 19.03) ''', (kundeid,))
                        kjopsid = cursor.lastrowid
                        conn.commit()
                        cursor.execute('''INSERT INTO billett VALUES (NULL, ?, ?, ?) ''', (kjopsid, forestillingID ,plassid,))
                        conn.commit()
            elif område == 'Parkett':
                radNr -=1
                seteNr = 0
                for char in line.strip():
                    if char == '0':
                        seteNr +=1
                        cursor.execute('''INSERT INTO plass VALUES (NULL, ?, ?, ?, ?) ''', (radNr, seteNr, område, sal_id,))
                        conn.commit()   
                    elif char == '1':
                        seteNr +=1
                        cursor.execute('''INSERT INTO plass VALUES (NULL, ?, ?, ?, ?) ''', (radNr, seteNr, område, sal_id,))
                        plassid = cursor.lastrowid
                        conn.commit()
                        cursor.execute(''' INSERT INTO billettKjop VALUES (NULL, ?, 14.38, 19.03) ''', (kundeid,))
                        kjopsid = cursor.lastrowid
                        conn.commit()
                        cursor.execute('''INSERT INTO billett VALUES (NULL, ?, ?, ?) ''', (kjopsid, forestillingID ,plassid,))
                        conn.commit()
    
setteStolerGamleScene("gamle-scene.txt")

conn.close()