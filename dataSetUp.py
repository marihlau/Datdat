import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()


cursor.execute('''INSERT INTO sal VALUES (NULL, "Hovedscenen", 516)''')

cursor.execute('''INSERT INTO  teaterStykke VALUES (NULL, "hei", "ola", 1)''')


conn.commit()
conn.close()