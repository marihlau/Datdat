import sqlite3

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

filePath = 'gamle-scene.txt'

cursor.execute('''insert into kundegruppe (gruppeid, gruppenavn) values (NULL, "Standardbruker")''')
gruppeid = cursor.lastrowid
cursor.execute('''insert into kundeprofil (kundeid, navn, mobilnr, adresse, gruppeid) values (NULL, "Standardbruker", "99999991", "Hovedscenen", ?)''', (gruppeid,))
kundeid = cursor.lastrowid
print(kundeid)
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