import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS "kanSe" (
	"gruppeID"	INTEGER NOT NULL,
	"stykkeID"	INTEGER NOT NULL,
	PRIMARY KEY("gruppeID","stykkeID"),
	FOREIGN KEY("stykkeID") REFERENCES "teaterStykke",
	FOREIGN KEY("gruppeID") REFERENCES "kundeGruppe"
)''')

cursor.execute('''INSERT INTO kanSe VALUES (3, 2)''')

conn.commit()
conn.close()