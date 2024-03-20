import sqlite3

def finn_forestillinger_på_dato(dato):

    db_file = "TrondelagTeater.db"  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
            SELECT teaterStykke.navn, COUNT(billett.plassID)
            FROM (forestilling LEFT JOIN billett ON forestilling.forestillingID = billett.forestillingID)
            JOIN teaterStykke on teaterStykke.stykkeID=forestilling.stykkeID
            WHERE forestilling.dato = ?
            GROUP BY forestilling.forestillingID
            ''', (dato,))
        
    resultater = cursor.fetchall()

    if resultater:
        print("Forestillinger som spilles på", dato, ":")
        for rad in resultater:
            print("  Til forestillingen,", rad[0], ", ble det solgt", rad[1], "billetter")
    else:
        print("Ingen forestillinger funnet på", dato)

    conn.close()

dato = input("Vennligst skriv inn datoen (D.M): ")
finn_forestillinger_på_dato(dato)
