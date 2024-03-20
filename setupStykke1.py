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

settInnRoller('Håkon Håkonsønn')
settInnRoller('Dagfinn Bonde')
settInnRoller('Jatgeir Skald')
settInnRoller('Sigrid')
settInnRoller('Ingebjørg') 
settInnRoller('Trønder') #byttet fra oppgaven til det som sto på nettsiden 
settInnRoller('Skule Jarl')
settInnRoller('Inga frå Vartejg')
settInnRoller('Paal Flida')
settInnRoller('Fru Ragnhild')
settInnRoller('Gregorius Jonssønn')
settInnRoller('Margrete')
settInnRoller('Biskop Nikolas')
settInnRoller('Peter')

conn.commit()

def setteAnsatte(navn, epost, ansatt_status):
    cursor.execute('''INSERT INTO ansatt VALUES (NULL, ?, ?, ?) ''', (navn, epost, ansatt_status,))

def setteSkuespiller(ansattID):
    if ansattID:
        cursor.execute('''INSERT INTO skuespiller VALUES (?) ''', (ansattID,))
    else:
        print("Fant ikke ansattID")

def spillerRolle(ansattID, rolleNavn):
    cursor.execute('''INSERT INTO spillerRolle VALUES (?, ?, ?) ''', (ansattID, stykke_id, rolleNavn))

#Setter inn skuespillere først som ansatte før vi henter ansattID og setter inn i skuespiller-tabellen
setteAnsatte('Arturo Scotti', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Håkon Håkonsønn')
conn.commit()
setteAnsatte('Ingunn Beate Strige Øyen', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Inga frå Vartejg')
conn.commit()
setteAnsatte('Hans Petter Nilsen', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Skule Jarl') 
conn.commit()
setteAnsatte('Madeleine Brandtzæg Nilsen', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Fru Ragnhild')
conn.commit()
setteAnsatte('Synnøve Fossum Eriksen', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Margrete')
conn.commit()
setteAnsatte('Emma Caroline Deichmann', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Sigrid')
spillerRolle(ansattID, 'Ingebjørg')
conn.commit()
setteAnsatte('Thomas Jensen Takyi', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Biskop Nikolas')
conn.commit()
setteAnsatte('Per Bogstad Gulliksen', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Gregorius Jonssønn')
conn.commit()
setteAnsatte('Isak Holmen Sørensen', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Paal Flida')
spillerRolle(ansattID, 'Trønder')
conn.commit()
setteAnsatte('Fabian Heideberg Lunde', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Baard Bratte')
spillerRolle(ansattID, 'Trønder')
conn.commit()
setteAnsatte('Emil Olafsson', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Dagfinn Bonde')
spillerRolle(ansattID, 'Jatgeir Skald')
conn.commit()
setteAnsatte('Snorre Ryen Tøndel', None, 'heltid')
ansattID = cursor.lastrowid
setteSkuespiller(ansattID)
spillerRolle(ansattID, 'Peter')
conn.commit()

def settOppgave(oppgaveNavn):
    cursor.execute('''INSERT INTO oppgave VALUES (?, ?) ''', (oppgaveNavn, stykke_id,))
#Setter inn oppgaver funnet på nettsiden under kunstnerisk lag
settOppgave('Regi')
settOppgave('Musikkutvelgelse')
settOppgave('Scenografi')
settOppgave('Kostymer')
settOppgave('Lysdesign')
settOppgave('Dramaturg')
conn.commit()

def giAnsattOppgave(ansattID, oppgaveNavn):
    cursor.execute('''INSERT INTO harOppgave VALUES (?, ?, ?) ''', (ansattID, oppgaveNavn, stykke_id))

#Setter inn ansatte som har andre oppgaver enn skuespiller og kobler de til oppgave
setteAnsatte('Yury Butusov', None, 'heltid')
ansattID = cursor.lastrowid
giAnsattOppgave(ansattID, 'Regi')
giAnsattOppgave(ansattID, 'Musikkutvelgelse')
conn.commit()
setteAnsatte('Aleksandr Shishkin-Hokusai', None, 'heltid')
ansattID = cursor.lastrowid
giAnsattOppgave(ansattID, 'Scenografi')
giAnsattOppgave(ansattID, 'Kostymer')
conn.commit()
setteAnsatte('Eivind Myren', None, 'heltid')
ansattID = cursor.lastrowid
giAnsattOppgave(ansattID, 'Lysdesign')
conn.commit()
setteAnsatte('Mina Rype Stokke', None, 'heltid')
ansattID = cursor.lastrowid
giAnsattOppgave(ansattID, 'Dramaturg')
conn.commit()

    
def settRolleTilAkt(aktNummer, rolleNavn):
    cursor.execute('''INSERT INTO erIAkt VALUES (?, ?, ?) ''', (aktNummer, rolleNavn, stykke_id,))

rolle_er_i_akt_oversikt = {
    'Håkon Håkonsønn': [1, 2, 3, 4, 5],
    'Dagfinn Bonde': [1, 2, 3, 4, 5],
    'Jatgeir Skald': [4],
    'Sigrid': [1, 2, 5],
    'Ingebjørg': [4],
    'Skule Jarl': [1, 2, 3, 4, 5],
    'Inga frå Vartejg': [1, 3],
    'Paal Flida': [1, 2, 3, 4, 5],
    'Ragnhild': [1, 5],
    'Gregorius Jonsson': [1, 2, 3, 4, 5],
    'Margrete': [1, 2, 3, 4, 5],
    'Biskop Nikolas': [1, 2, 3],
    'Peter': [3, 4, 5]
}
for rolle, akt in rolle_er_i_akt_oversikt.items():
    for aktNummer in akt:
        settRolleTilAkt(aktNummer, rolle)

def sjekkSetup(sal):
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
    sjekkSal = cursor.fetchone()

    if sjekkSal == None:
        cursor.execute('''insert into sal (navn, kapasitet) values ("Hovedscenen", 516) returning salid''')
        salid = cursor.fetchone()[0]
        conn.commit()
    else:
        salid = sjekkSal[0]

    sjekkrad = list('01x')
    radnr = 20
    setenr = 515
    dato = None
    omraade = None
    linenum = 1
    galleriline = 1

    for line in lines:
        s = set(line.strip())
        if linenum == 1:
            dato = line.split()[1]
        elif all(letter not in s for letter in sjekkrad):
            omraade = line.strip()
        else:                        
            for x in line.strip():
                if x == '0':
                    cursor.execute('''insert into plass (plassid, radnr, stolnr, omraade, salid) values (NULL, ?, ?, ?, ?)''', (radnr, setenr, omraade, salid,))
                    conn.commit()
                elif x == '1':
                    cursor.execute('''insert into plass (plassid, radnr, stolnr, omraade, salid) values (NULL, ?, ?, ?, ?) ''', (radnr, setenr, omraade, salid,))
                    plassid = cursor.lastrowid
                    conn.commit()
                    cursor.execute(''' insert into billettKjop (kjopsid, kundeid, tid, dato) values (NULL, ?, 14.38, 19.03) ''', (kundeid,))
                    kjopsid = cursor.lastrowid
                    conn.commit()
                    cursor.execute('''insert into billett (billettid, kjopsid, forestillingid, plassid) values (NULL, ?, ?, ?) ''', (kjopsid, forestillingID ,plassid,))
                    conn.commit()
                setenr += 1

            if omraade == 'Galleri':                
                if galleriline == 2:
                    setenr -= (2*10)
                    radnr -= 1
                if galleriline == 4:
                    setenr -= (10+28)
                    radnr -=1
                galleriline+= 1
            else:
                setenr -= (2*28)
                radnr -= 1
        
        linenum += 1

def readHovedscenenSetup(file):

    with open(file, 'r') as f:
        lines = f.readlines()

    check = sjekkSetup('Hovedscenen')

    if check == 0:
        setupHovedscenen(lines)


readHovedscenenSetup('hovedscenen.txt')

conn.close()