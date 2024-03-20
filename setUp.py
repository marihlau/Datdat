import sqlite3

db_file = "TrondelagTeater.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

with open('fjern_alle_tabeller.sql') as fjern_tabeller: #fjerner alle tabellene.
    sql_script = fjern_tabeller.read()
    
cursor.executescript(sql_script)
conn.commit()

with open('Prosjekt-SQL-gruppe-201.sql') as sql_file: #oppretter alle tabellene.
    sql_script = sql_file.read()
    
cursor.executescript(sql_script)

conn.commit()
conn.close()