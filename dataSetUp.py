import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()


salID_data=(NULL)
cursor.execute('''INSERT INTO sal VALUES (?, "Hovedscenen", 516)''', salID_data)

salID=conn.execute("SELECT last_insert_rowid()").fetchone()[0]

teaterStykke_data=( salID)
cursor.execute('''INSERT INTO  teaterStykke VALUES (NULL, "hei", "ola", ?)''', teaterStykke_data)


conn.commit()
conn.close()