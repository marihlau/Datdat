import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()




cursor.execute('''INSERT INTO sal VALUES (NULL, "Hovedscenen", 516)''')
conn.commit()

sal_id = cursor.lastrowid

cursor.execute('''INSERT INTO  teaterStykke VALUES (NULL, "hei", "ola", 1)''')


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