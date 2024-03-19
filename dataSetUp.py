import sqlite3

db_file = "TrondelagTeater.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()




cursor.execute('''INSERT INTO sal VALUES (NULL, "Hovedscenen", 516)''')
conn.commit()

sal_id = cursor.lastrowid

cursor.execute('''INSERT INTO teaterStykke VALUES (NULL, "Kongsemnene", "Ibsen", ?)''', (sal_id,))
conn.commit()

stykke_id = cursor.lastrowid

def settInnAktKongsemnene(tittel):
    for i in range(1, 6):
        cursor.execute('''INSERT INTO akt VALUES (?, ?, ?) ''', (stykke_id, i, i,))
        conn.commit()
    
settInnAktKongsemnene("Kongsemnene")

def settInnForestilling (start_tid, dato):
    cursor.execute('''INSERT INTO forestilling VALUES (NULL, ?, ?, ?) ''', (start_tid, dato, stykke_id))

settInnForestilling(1.2, 19.0)
settInnForestilling(2.2, 19.0)
settInnForestilling(3.2, 19.0)
forestillingID = cursor.lastrowid
settInnForestilling(5.2, 19.0)
settInnForestilling(6.2, 19.0)

def settInnRoller (navn):
    cursor.execute('''INSERT INTO rolle VALUES (?,?) ''', (navn, stykke_id,))

settInnRoller('Håkon Håkonson')
settInnRoller('Dagfinn Bonde')
settInnRoller('Jatgeir Skald')
settInnRoller('Sigrid')
settInnRoller('Ingebjørg') 
settInnRoller('Trønder') #byttet fra oppgaven til det som sto på nettsiden 
settInnRoller('Skule Jarl')
settInnRoller('Inga frå Vartejg')
settInnRoller('Paal Flida')
settInnRoller('Ragnhild')
settInnRoller('Gregorius Jonssønn')
settInnRoller('Margrete')
settInnRoller('Biskop Nikolas')
settInnRoller('Peter')

def setteAnsatte(navn, epost, ansatt_status):
    cursor.execute('''INSERT INTO ansatt VALUES (NULL, ?, ?, ?) ''', (navn, epost, ansatt_status,))

# setteAnsatte("Arturo Scotti", "")

cursor.execute('''insert into kundegruppe (gruppeid, gruppenavn) values (NULL, "Standardbruker")''')
gruppeid = cursor.lastrowid
cursor.execute('''insert into kundeprofil (kundeid, navn, mobilnr, adresse, gruppeid) values (NULL, "Standardbruker", "99999999", "Hovedscenen", ?)''', (gruppeid,))
kundeid = cursor.lastrowid
print(kundeid)
conn.commit()

def checkSetup(sal):
    cursor.execute('''select count(*) = s.kapasitet from plass p, sal s where p.salid = s.salid and s.navn = ?''', (sal,))
    check = cursor.fetchone()
    returnvalue = 0 if check[0] == None else check[0]
    return returnvalue


def setupHovedscenen(lines):
        
    #Opprett sal i databasen hvis ikke finnes

    cursor.execute('''select salid from sal where navn = "Hovedscenen"''')
    checkSal = cursor.fetchone()

    if checkSal == None:
        cursor.execute('''insert into sal (navn, kapasitet) values ("Hovedscenen", 516) returning salid''')
        salid = cursor.fetchone()[0]
        conn.commit()
    else:
        salid = checkSal[0]

    checkrow = list('01x')
    rownum = 20
    seatnum = 515
    date = None
    area = None
    linenum = 1
    galleriline = 1

    for line in lines:
        s = set(line.strip())
        if linenum == 1:
            date = line.split()[1]
        elif all(letter not in s for letter in checkrow):
            area = line.strip()
        else:                        
            #seatsinrow = len(s)
            for x in line.strip():
                if x == '0':
                    cursor.execute('''insert into plass (plassid, radnr, stolnr, omraade, salid) values (NULL, ?, ?, ?, ?)''', (rownum, seatnum, area, salid,))
                    conn.commit()
                elif x == '1':
                    cursor.execute('''insert into plass (plassid, radnr, stolnr, omraade, salid) values (NULL, ?, ?, ?, ?) ''', (rownum, seatnum, area, salid,))
                    plassid = cursor.lastrowid
                    conn.commit()
                    cursor.execute(''' insert into billettKjop (kjopsid, kundeid, tid, dato) values (NULL, ?, 14.38, 19.03) ''', (kundeid,))
                    kjopsid = cursor.lastrowid
                    conn.commit()
                    cursor.execute('''insert into billett (billettid, kjopsid, forestillingid, plassid) values (NULL, ?, ?, ?) ''', (kjopsid, forestillingID ,plassid,))
                    conn.commit()
                seatnum += 1

            if area == 'Galleri':                
                if galleriline == 2:
                    seatnum -= (2*10)
                    rownum -= 1
                if galleriline == 4:
                    seatnum -= (10+28)
                    rownum -=1
                galleriline+= 1
            else:
                seatnum -= (2*28)
                rownum -= 1
        
        linenum += 1

def readHovedscenenSetup(file):

    with open(file, 'r') as f:
        lines = f.readlines()

    check = checkSetup('Hovedscenen')

    if check == 0:
        setupHovedscenen(lines)


readHovedscenenSetup('hovedscenen.txt')
 

cursor.execute('''INSERT INTO sal VALUES (NULL, "Gamle scene", 332)''')
conn.commit()

sal_id = cursor.lastrowid

cursor.execute('''INSERT INTO teaterStykke VALUES (NULL, "Størst av alt er kjærligheten", "Petersen", ?)''', (sal_id,))
conn.commit()

stykke_id = cursor.lastrowid

settInnForestilling(3.2, 18.5)
forestillingID = cursor.lastrowid
settInnForestilling(6.2, 18.5)
settInnForestilling(7.2, 18.5)
settInnForestilling(12.2, 18.5)
settInnForestilling(13.2, 18.5)
settInnForestilling(14.2, 18.5)

filePath = 'gamle-scene.txt'

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