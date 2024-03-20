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

#Funksjon som setter inn roller
def settInnRoller (navn):
    cursor.execute('''INSERT INTO rolle VALUES (?,?) ''', (navn, stykke_id,))

#Rollene som blir satt inn
settInnRoller('Sunniva Du Mond Nordal')
settInnRoller('Jo Saberniak')
settInnRoller('Marte M. Steinholt')
settInnRoller('Tor Ivar Hagen')
settInnRoller('Trond-Ove Skrødal')
settInnRoller('Natalie Grøndahl Tangen')
settInnRoller('Åsmund Flaten')
conn.commit()

#Funksjon som setter inn ansatte
def setteAnsatte(navn, epost, ansatt_status):
    cursor.execute('''INSERT INTO ansatt VALUES (NULL, ?, ?, ?) ''', (navn, epost, ansatt_status,))

#Funksjon som setter inn skuespillere
def setteSkuespiller(ansattID):
    if ansattID:
        cursor.execute('''INSERT INTO skuespiller VALUES (?) ''', (ansattID,))
    else:
        print("Fant ikke ansattID")

#Funksjon som setter inn i spillerRolle tabellen
def settSpillerRolle(ansattID, rolleNavn):
    cursor.execute('''INSERT INTO spillerRolle VALUES (?,?,?)''', (ansattID, stykke_id, rolleNavn,))

#Setter inn verdiene for ansatte som er skuespillere
setteAnsatte('Sunniva Du Mond Nordal', None, 'heltid')
setteSkuespiller(cursor.lastrowid)
settSpillerRolle(cursor.lastrowid, 'Sunniva Du Mond Nordal')
conn.commit()
setteAnsatte('Jo Saberniak', None, 'heltid')
setteSkuespiller(cursor.lastrowid)
settSpillerRolle(cursor.lastrowid, 'Jo Saberniak')
conn.commit()
setteAnsatte('Marte M. Steinholt', None, 'heltid')
setteSkuespiller(cursor.lastrowid)
settSpillerRolle(cursor.lastrowid,'Marte M. Steinholt' )
conn.commit()
setteAnsatte('Tor Ivar Hagen', None, 'heltid')
setteSkuespiller(cursor.lastrowid)
settSpillerRolle(cursor.lastrowid, 'Tor Ivar Hagen')
conn.commit()
setteAnsatte('Trond-Ove Skrødal', None, 'heltid')
setteSkuespiller(cursor.lastrowid)
settSpillerRolle(cursor.lastrowid, 'Trond-Ove Skrødal')
conn.commit()
setteAnsatte('Natalie Grøndahl Tangen', None, 'heltid')
setteSkuespiller(cursor.lastrowid)
settSpillerRolle(cursor.lastrowid,'Natalie Grøndahl Tangen' )
conn.commit()
setteAnsatte('Åsmund Flaten', None, 'heltid')
setteSkuespiller(cursor.lastrowid)
settSpillerRolle(cursor.lastrowid, 'Åsmund Flaten')
conn.commit()

#Funksjon som setter inn i erIAkt tabellen
def settErIAkt(aktNR, navn):
    cursor.execute('''INSERT INTO erIAkt VALUES (?,?,?)''',(aktNR, navn, stykke_id,))

#Setter inn verdier i erIAkt
settErIAkt(1,'Sunniva Du Mond Nordal')
settErIAkt(1,'Jo Saberniak')
settErIAkt(1,'Marte M. Steinholt')
settErIAkt(1,'Tor Ivar Hagen' )
settErIAkt(1, 'Trond-Ove Skrødal')
settErIAkt(1, 'Natalie Grøndahl Tangen')
settErIAkt(1,'Åsmund Flaten' )
conn.commit()

#Funksjon som setter inn oppgaver
def settOppgave(oppgaveNavn):
    cursor.execute('''INSERT INTO oppgave VALUES (?,?)''', (oppgaveNavn, stykke_id,))

#Setter inn oppgaver
settOppgave('Regi')
settOppgave('Scenografi')
settOppgave('Kostymer')
settOppgave('Musikalsk ansvarlig')
settOppgave('Lysdesign')
settOppgave('Dramaturg')
conn.commit()

#Funksjon som setter inn i harOppgave tabellen
def settHarOppgave(ansattID, oppgaveNavn):
    cursor.execute('''INSERT INTO harOppgave VALUES (?,?,?)''', (ansattID, oppgaveNavn, stykke_id,))

#Setter inn verdier for ansatte som har andre oppgaver enn skuespillere, og tilegner dem oppgaven
setteAnsatte('Jonas Corell Petersen', None, 'heltid')
ansattID = cursor.lastrowid
settHarOppgave(ansattID, 'Regi')
conn.commit()
setteAnsatte('David Gehrt', None, 'heltid')
ansattID = cursor.lastrowid
settHarOppgave(ansattID, 'Scenograf')
settHarOppgave(ansattID, 'Kostymer')
conn.commit()
setteAnsatte('Gaute Tønder', None, 'heltid')
ansattID = cursor.lastrowid
settHarOppgave(ansattID, 'Musikalsk ansvarlig')
conn.commit()
setteAnsatte('Magnus Mikaelsen', None, 'heltid')
ansattID = cursor.lastrowid
settHarOppgave(ansattID, 'Lysdesign')
conn.commit()
setteAnsatte('Kristoffer Spender', None, 'heltid')
ansattID = cursor.lastrowid
settHarOppgave(ansattID, 'Dramaturg')
conn.commit()

filePath = 'gamle-scene.txt'
#Setter inn stolene på gamle scene
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