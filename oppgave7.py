import sqlite3

def finn_skuespiller_navn(navn):

    db_file = "test.db"  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
            SELECT a1.navn, a2.navn, teaterstykke.navn
            FROM 
                   (((ansatt AS a1 JOIN spillerRolle AS spiller1 ON a1.ansattID=spiller1.ansattID)
                   JOIN erIAKT AS akt1 ON spiller1.stykkeID=akt1.stykkeID) AS ansatt1
                JOIN
                   ((ansatt AS a2 JOIN spillerRolle AS spiller2 ON a2.ansattID=spiller2.ansattID)
                   JOIN erIAKT AS akt2 ON spiller2.stykkeID=akt2.stykkeID) AS ansatt2
                ON ansatt1.aktNR=ansatt2.aktNR)
                JOIN teaterstykke ON teaterstykke.stykkeID=ansatt1.stykkeID
            WHERE ansatt1.navn=?
            GROUP BY ansatt1.ansattID
            ''', (navn,))
    
    resultater = cursor.fetchall()

    if resultater:
        print("Skuespiller med", navn, ":")
        for rad in resultater:
            print("  Spilte med", rad[1])
            print(" i skuespillet ", rad[2] )
    else:
        print("Ingen skuespillere funnet med navn ", navn)

    conn.close()

navn = input("Skriv inn navnet på skuespilleren: ")
finn_skuespiller_navn(navn)
