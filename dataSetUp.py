import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()




cursor.execute('''INSERT INTO sal VALUES (NULL, "Hovedscenen", 516)''')
conn.commit()

sal_id = cursor.lastrowid

cursor.execute('''INSERT INTO teaterStykke VALUES (NULL, "Kongsemnene", "Ibsen", ?)''', (sal_id,))
conn.commit()

conn.close()