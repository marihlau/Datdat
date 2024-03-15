import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS kanSe (
	gruppeID	INTEGER NOT NULL,
	stykkeID	INTEGER NOT NULL,
	PRIMARY KEY(gruppeID,stykkeID),
	FOREIGN KEY(stykkeID) REFERENCES teaterStykke,
	FOREIGN KEY(gruppeID) REFERENCES kundeGruppe
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS oppgave (
	oppgaveNavn	TEXT NOT NULL,
	stykkeID	INTEGER NOT NULL,
	PRIMARY KEY(oppgaveNavn,stykkeID),
	FOREIGN KEY(stykkeID) REFERENCES teaterStykke
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS skuespiler (
	ansattID	INTEGER NOT NULL,
	PRIMARY KEY(ansattID),
	FOREIGN KEY(ansattID) REFERENCES ansatt
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS rolle (
	navn	TEXT NOT NULL,
	stykkeID	INTEGER NOT NULL,
	PRIMARY KEY(stykkeID,navn),
	FOREIGN KEY(stykkeID) REFERENCES teaterStykke
)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS spillerRolle (
	ansattID	INTEGER NOT NULL,
	stykkeID	INTEGER NOT NULL,
	navn	TEXT NOT NULL,
	PRIMARY KEY(navn,stykkeID,ansattID),
	FOREIGN KEY(ansattID) REFERENCES ansatt,
	FOREIGN KEY(navn) REFERENCES rolle,
	FOREIGN KEY(stykkeID) REFERENCES teaterStykke
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS harOppgave (
	ansattID	INTEGER NOT NULL,
	oppgaveNavn	TEXT NOT NULL,
	stykkeID	INTEGER NOT NULL,
	PRIMARY KEY(ansattID,oppgaveNavn,stykkeID),
	FOREIGN KEY(stykkeID) REFERENCES teaterStykke,
	FOREIGN KEY(oppgaveNavn) REFERENCES oppgave,
	FOREIGN KEY(ansattID) REFERENCES ansatt
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS erIAkt (
	aktNR	INTEGER NOT NULL,
	navn    TEXT NOT NULL,
	stykkeID	INTEGER NOT NULL,
	PRIMARY KEY(aktNR,stykkeID,navn),
	FOREIGN KEY(aktNR) REFERENCES akt,
	FOREIGN KEY(navn) REFERENCES rolle
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS akt (
	stykkeID	INTEGER NOT NULL,
	aktNR	INTEGER NOT NULL,
	navn	TEXT,
	PRIMARY KEY(stykkeID,aktNR),
	FOREIGN KEY(stykkeID) REFERENCES teaterStykke
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ansatt (
	ansattID	INTEGER NOT NULL,
	navn	TEXT NOT NULL,
	epost	TEXT NOT NULL UNIQUE,
	ansattStatus	TEXT NOT NULL,
	PRIMARY KEY(ansattID)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS billet (
	billetID	INTEGER NOT NULL,
	kjøpsID	INTEGER NOT NULL,
	forestillingID	INTEGER NOT NULL,
	plassID	INTEGER NOT NULL,
	PRIMARY KEY(billetID),
	FOREIGN KEY(kjøpsID) REFERENCES billetKjøp,
	FOREIGN KEY(plassID) REFERENCES plass,
	FOREIGN KEY(forestillingID) REFERENCES forestilling
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS billetKjøp (
	kjøpsID	INTEGER NOT NULL,
	kundeID	INTEGER NOT NULL,
	tid	INTEGER NOT NULL,
	dato	INTEGER NOT NULL,
	PRIMARY KEY(kjøpsID),
	FOREIGN KEY(kundeID) REFERENCES kundeProfil
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS forestilling (
	forestillingID	INTEGER NOT NULL,
	startTid	INTEGER NOT NULL,
	dato	INTEGER NOT NULL,
	stykkeID	INTEGER NOT NULL,
	PRIMARY KEY(forestillingID)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS kundeGruppe (
	gruppeID	INTEGER NOT NULL,
	gruppeNavn	TEXT NOT NULL,
	PRIMARY KEY(gruppeID)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS kundeProfil (
	kundeID	INTEGER NOT NULL,
	navn	TEXT NOT NULL,
	mobilNR	INTEGER NOT NULL UNIQUE,
	adresse	TEXT NOT NULL,
	gruppeID	INTEGER NOT NULL,
	PRIMARY KEY(kundeID),
	FOREIGN KEY(gruppeID) REFERENCES kundeGruppe
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS plass (
	plassID	INTEGER NOT NULL,
	radNR	INTEGER NOT NULL,
	stolNR	INTEGER NOT NULL,
	område  TEXT,
	salID	INTEGER NOT NULL,
	PRIMARY KEY(plassID),
	FOREIGN KEY(salID) REFERENCES sal
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS sal (
	salID	INTEGER NOT NULL PRIMARY KEY,
	navn	TEXT NOT NULL,
	kapasitet	INTEGER NOT NULL
	
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS teaterStykke (
	stykkeID	INTEGER NOT NULL,
	navn	TEXT,
	forfatter	TEXT,
	salID	INTEGER NOT NULL,
	PRIMARY KEY(stykkeID),
	FOREIGN KEY(salID) REFERENCES sal
)
''')


conn.commit()
conn.close()