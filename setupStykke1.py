import sqlite3
kundegrupper = ["ordinær", "honnør", "student", "barn"]
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

settInnForestilling(1900, 1.2)
settInnForestilling(1900, 2.2)
settInnForestilling(1900, 3.2)
settInnForestilling(1900, 5.2)
settInnForestilling(1900, 6.2)

conn.commit()

def settOppkanSeKongsemnene():

    cursor.execute('''SELECT stykkeID FROM teaterStykke WHERE navn = ?''', ("Kongsemnene",))
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
            cursor.execute('''INSERT INTO kanSe VALUES (?, ?, 450)''', (gruppeID, stykkeID,))
        elif gruppe == "honnør":
            cursor.execute('''INSERT INTO kanSe VALUES (?, ?, 380)''', (gruppeID, stykkeID,))
        elif gruppe == "student":
            cursor.execute('''INSERT INTO kanSe VALUES (?, ?, 280)''', (gruppeID, stykkeID,))

settOppkanSeKongsemnene()

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

conn.commit()

def setteAnsatte(navn, epost, ansatt_status):
    cursor.execute('''INSERT INTO ansatt VALUES (NULL, ?, ?, ?) ''', (navn, epost, ansatt_status,))



def checkSetup(sal):
    cursor.execute('''select count(*) = s.kapasitet from plass p, sal s where p.salid = s.salid and s.navn = ?''', (sal,))
    check = cursor.fetchone()
    returnvalue = 0 if check[0] == None else check[0]
    return returnvalue

#Henter ut info om standarbruker:
cursor.execute('''SELECT kundeID FROM kundeProfil WHERE navn = ?''', ("Standardbruker",))  
sjekkStandardbruker = cursor.fetchone()
if sjekkStandardbruker:
    kundeid = sjekkStandardbruker[0]
#Henter ut forestillingID for en abitrær forestilling av Kongsemnene
cursor.execute('''SELECT forestillingID FROM forestilling WHERE stykkeID = ?''', (stykke_id,))
sjekForestilling = cursor.fetchone()
if sjekForestilling:
    forestillingID = sjekForestilling[0]


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

conn.close()