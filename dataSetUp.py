import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()




cursor.execute('''INSERT INTO sal VALUES (NULL, "Hovedscenen", 516)''')
conn.commit()

sal_id = cursor.lastrowid

cursor.execute('''INSERT INTO teaterStykke VALUES (NULL, "Kongsemnene", "Ibsen", ?)''', (sal_id,))
conn.commit()

stykke_id = cursor.lastrowid

cursor.execute('''INSERT INTO akt VALUES (?, NULL, "1") ''', (stykke_id))
conn.commit()

cursor.execute('''INSERT INTO akt VALUES (?, NULL, "2") ''', (stykke_id))
conn.commit()

cursor.execute('''INSERT INTO akt VALUES (?, NULL, "3") ''', (stykke_id))
conn.commit()

cursor.execute('''INSERT INTO akt VALUES (?, NULL, "4") ''', (stykke_id))
conn.commit()

cursor.execute('''INSERT INTO akt VALUES (?, NULL, "5") ''', (stykke_id))
conn.commit()

def settInnForestilling (start_tid, dato):
    cursor.execute('''INSERT INTO forestilling VALUES (NULL, ?, ?, ?) ''', (start_tid, dato, stykke_id))

settInnForestilling(1.2, 19.0)
settInnForestilling(2.2, 19.0)
settInnForestilling(3.2, 19.0)
settInnForestilling(5.2, 19.0)
settInnForestilling(6.2, 19.0)

def settInnRoller (navn):
    cursor.execute('''INSERT INTO rolle VALUES (?,?) ''', (navn, stykke_id))

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
    cursor.execute('''INSERT INTO ansatt VALUES (NULL, ?, ?, ?) ''', (navn, epost, ansatt_status))

setteAnsatte("Arturo Scotti", "")


filePath = 'hovedscenen.txt'

def setteStolerHovedscenen(filePath):
    #Åpner filen og leser filen 
    with open(filePath, 'r') as file:
        lines = file.readlines()

    område = None
    radNr = 0
    seteNr = 1   

    for line in lines:
        # Ser om vi er i galleri eller parkett området
        if 'Galleri' in line:
            område = 'Galleri'
            radNr = 0
            seteNr = 505
        elif 'Parkett' in line:
            område = 'Parkett'
            radNr = 19
            seteNr = 505
        
        # Alle andre linjer inneholder data om seter, siden vi starter på toppen må vi telle oss nedover
        else:
            if område == 'Parkett':
                radNr -= 1
                seteNr = seteNr-28
                if radNr <= 17:
                    seteNr = seteNr - 28
                    #Må fjerne 28 seter til for at vi skal starte med riktig sete
                for char in line.strip():
                    if char in '01x':
                        seteNr += 1 
                        #Øker seteNr med 1 uansett om det er et sete der eller ikke, i henhold til vedlegget om hovedscenen 
                        if char in '01':
                            cursor.execute('''INSERT INTO plass (NULL, ?, ?, ?, ?)''', (radNr, seteNr, område, sal_id))
                            conn.commit()

            elif område == 'Galleri':
                radNr += 1
                for char in line.strip():
                    if char in '01':
                        seteNr += 1
                        cursor.execute('''INSERT INTO plass (NULL, ?, ?, ?, ?)''', (radNr, seteNr, område, sal_id))
                        conn.commit()




#Denne funksjonen ble ganske krunglete siden vi må starte bakerst i salen og jobbe oss fremover 

cursor.execute('''INSERT INTO sal VALUES (NULL, "Gamle scene", 332)''')
conn.commit()

sal_id = cursor.lastrowid

cursor.execute('''INSERT INTO teaterStykke VALUES (NULL, "Størst av alt er kjærligheten", "Petersen", ?)''', (sal_id))
conn.commit()

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
                    if char in '01':
                        seteNr +=1
                        cursor.execute('''INSERT INTO plass (NULL, ?, ?, ?, ?) ''', (radNr, seteNr, område, sal_id))
                        conn.commit()
            elif område == 'Balkong':
                radNr -=1
                seteNr = 0
                for char in line.strip():
                    if char in '01':
                        seteNr +=1
                        cursor.execute('''INSERT INTO plass (NULL, ?, ?, ?, ?) ''', (radNr, seteNr, område, sal_id))  
                        conn.commit()
            elif område == 'Parkett':
                radNr -=1
                seteNr = 0
                for char in line.strip():
                    if char in '01':
                        seteNr +=1
                        cursor.execute('''INSERT INTO plass (NULL, ?, ?, ?, ?) ''', (radNr, seteNr, område, sal_id))
                        conn.commit()   

conn.close()