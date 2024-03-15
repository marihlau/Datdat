import sqlite3

db_file = "test.db"  # Legg til riktig filtype for SQLite-databasen

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT, birthday DATE)''')

cursor.execute('''INSERT INTO person VALUES (3, 'Ola Nordmann', '2002-02-02')''')

conn.commit()
conn.close()


# from sqlite3 import Error

# def create_connection(db_file):

#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print("noe skjedde")

#         cursor = conn.cursor()
#         cursor.execute( )

    
#     except Error as e:
#         print("Funka ikke")
#     finally:
#         if conn:
#             conn.commit()
#             conn.close()


# if __name__ == '__main__':
#     create_connection(db_file)