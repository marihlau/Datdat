import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT, birthday DATE)''')

cursor.execute('''INSERT INTO person VALUES (3, 'Ola Nordmann', '2002-02-02')''')

conn.commit()
conn.close()


