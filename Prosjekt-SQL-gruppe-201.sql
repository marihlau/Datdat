BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "kanSe" (
	"gruppeID"	INTEGER NOT NULL,
	"stykkeID"	INTEGER NOT NULL,
	"pris"	INTEGER,
	PRIMARY KEY("gruppeID","stykkeID"),
	FOREIGN KEY("stykkeID") REFERENCES "teaterStykke",
	FOREIGN KEY("gruppeID") REFERENCES "kundeGruppe"
);
CREATE TABLE IF NOT EXISTS "oppgave" (
	"oppgaveNavn"	TEXT NOT NULL,
	"stykkeID"	INTEGER NOT NULL,
	PRIMARY KEY("oppgaveNavn","stykkeID"),
	FOREIGN KEY("stykkeID") REFERENCES "teaterStykke"
);
CREATE TABLE IF NOT EXISTS "skuespiller" (
	"ansattID"	INTEGER NOT NULL,
	PRIMARY KEY("ansattID"),
	FOREIGN KEY("ansattID") REFERENCES "ansatt"
);
CREATE TABLE IF NOT EXISTS "rolle" (
	"navn"	TEXT NOT NULL,
	"stykkeID"	INTEGER NOT NULL,
	PRIMARY KEY("stykkeID","navn"),
	FOREIGN KEY("stykkeID") REFERENCES "teaterStykke"
);
CREATE TABLE IF NOT EXISTS "spillerRolle" (
	"ansattID"	INTEGER NOT NULL,
	"stykkeID"	INTEGER NOT NULL,
	"navn"	TEXT NOT NULL,
	PRIMARY KEY("navn","stykkeID","ansattID"),
	FOREIGN KEY("ansattID") REFERENCES "ansatt",
	FOREIGN KEY("navn") REFERENCES "rolle",
	FOREIGN KEY("stykkeID") REFERENCES "teaterStykke"
);
CREATE TABLE IF NOT EXISTS "harOppgave" (
	"ansattID"	INTEGER NOT NULL,
	"oppgaveNavn"	TEXT NOT NULL,
	"stykkeID"	INTEGER NOT NULL,
	PRIMARY KEY("ansattID","oppgaveNavn","stykkeID"),
	FOREIGN KEY("stykkeID") REFERENCES "teaterStykke",
	FOREIGN KEY("oppgaveNavn") REFERENCES "oppgave",
	FOREIGN KEY("ansattID") REFERENCES "ansatt"
);
CREATE TABLE IF NOT EXISTS "erIAkt" (
	"aktNR"	INTEGER NOT NULL,
	"navn"	TEXT NOT NULL,
	"stykkeID"	INTEGER NOT NULL,
	PRIMARY KEY("aktNR","stykkeID","navn"),
	FOREIGN KEY("aktNR") REFERENCES "akt",
	FOREIGN KEY("navn") REFERENCES "rolle"
);
CREATE TABLE IF NOT EXISTS "akt" (
	"stykkeID"	INTEGER NOT NULL,
	"aktNR"	INTEGER NOT NULL,
	"navn"	TEXT,
	PRIMARY KEY("stykkeID","aktNR"),
	FOREIGN KEY("stykkeID") REFERENCES "teaterStykke"
);
CREATE TABLE IF NOT EXISTS "ansatt" (
	"ansattID"	INTEGER NOT NULL,
	"navn"	TEXT NOT NULL,
	"epost"	TEXT NOT NULL UNIQUE,
	"ansattStatus"	TEXT NOT NULL,
	PRIMARY KEY("ansattID")
);

CREATE TABLE IF NOT EXISTS "billett" (
	"billettID"	INTEGER NOT NULL,
	"kjopsID"	INTEGER NOT NULL,
	"forestillingID"	INTEGER NOT NULL,
	"plassID"	INTEGER NOT NULL,
	PRIMARY KEY("billettID"),
	FOREIGN KEY("kjopsID") REFERENCES "billetKjop",
	FOREIGN KEY("plassID") REFERENCES "plass",
	FOREIGN KEY("forestillingID") REFERENCES "forestilling"
);
CREATE TABLE IF NOT EXISTS "billettKjop" (
	"kjopsID"	INTEGER NOT NULL,
	"kundeID"	INTEGER NOT NULL,
	"tid"	INTEGER NOT NULL,
	"dato"	INTEGER NOT NULL,
	PRIMARY KEY("kjopsID"),
	FOREIGN KEY("kundeID") REFERENCES "kundeProfil"
);
CREATE TABLE IF NOT EXISTS "forestilling" (
	"forestillingID"	INTEGER NOT NULL,
	"startTid"	INTEGER NOT NULL,
	"dato"	INTEGER NOT NULL,
	"stykkeID"	INTEGER NOT NULL,
	PRIMARY KEY("forestillingID")
);
CREATE TABLE IF NOT EXISTS "kundeGruppe" (
	"gruppeID"	INTEGER NOT NULL,
	"gruppeNavn"	TEXT NOT NULL,
	PRIMARY KEY("gruppeID")
);
CREATE TABLE IF NOT EXISTS "kundeProfil" (
	"kundeID"	INTEGER NOT NULL,
	"navn"	TEXT NOT NULL,
	"mobilNR"	INTEGER NOT NULL UNIQUE,
	"adresse"	TEXT NOT NULL,
	"gruppeID"	INTEGER NOT NULL,
	PRIMARY KEY("kundeID"),
	FOREIGN KEY("gruppeID") REFERENCES "kundeGruppe"
);
CREATE TABLE IF NOT EXISTS "plass" (
	"plassID"	INTEGER NOT NULL,
	"radNR"	INTEGER NOT NULL,
	"stolNR"	INTEGER NOT NULL,
	"omraade"	TEXT,
	"salID"	INTEGER NOT NULL,
	PRIMARY KEY("plassID"),
	FOREIGN KEY("salID") REFERENCES "sal"
);
CREATE TABLE IF NOT EXISTS "sal" (
	"salID"	INTEGER NOT NULL,
	"navn"	TEXT NOT NULL,
	"kapasitet"	INTEGER NOT NULL,
	PRIMARY KEY("salID")
);
CREATE TABLE IF NOT EXISTS "teaterStykke" (
	"stykkeID"	INTEGER NOT NULL,
	"navn"	TEXT,
	"forfatter"	TEXT,
	"salID"	INTEGER NOT NULL,
	PRIMARY KEY("stykkeID"),
	FOREIGN KEY("salID") REFERENCES "sal"
);
COMMIT;

