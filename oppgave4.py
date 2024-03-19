import sqlite3

def finn_forestillinger_på_dato(dato):

    db_file = "test.db"  
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
        print("Forestillinger på", dato, ":")
        for rad in resultater:
            print("- Fore∏stilling:", rad[0])
            print("  Antall billetter solgt:", rad[1])
    else:
        print("Ingen forestillinger funnet på", dato)

    conn.close()

dato = input("Vennligst skriv inn datoen (YYYY-MM-DD): ")
finn_forestillinger_på_dato(dato)
