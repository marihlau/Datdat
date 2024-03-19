import sqlite3

def finn_skuespiller_navn(navn):

    db_file = "test.db"  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
            SELECT a1.navn, a2.navn, teaterStykke.navn
            FROM (((ansatt AS a1 JOIN spillerRolle ON a1.ansattID=spillerRolle.ansattID)
                   JOIN teaterStykke ON spillerRolle.stykkeID=teaterStykke.stykkeID) as ansatt1
                JOIN 
                   (ansatt AS a2 JOIN spillerRolle ON a2.ansattID=spillerRolle.ansattID) as ansatt2 
                ON  
                    ansatt1.stykkeID=ansatt2.stykkeID)
                JOIN teaterSTykke ON ansatt1.stykkeID=teaterStykke.stykkeID
            WHERE ansatt.navn=?
            GROUP BY ansatt.ansattID
            ''', (navn,))
        
    resultater = cursor.fetchall()

    if resultater:
        print("Skuespillere på", navn, ":")
        for rad in resultater:
            print("- Skuespiller:", rad[0])
            print("  Spilt med:", rad[1])
    else:
        print("Ingen skuespillere funnet med ", navn)

    conn.close()

navn = input("Skriv inn navnet på skuespilleren: ")
finn_skuespiller_navn(navn)
