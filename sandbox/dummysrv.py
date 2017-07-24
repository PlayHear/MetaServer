#Author : Supragya Raj
#Dummy server

import sqlite3
connection = sqlite3.connect("database.db")

cur = connection.cursor()

#Create table
cur.execute('''CREATE TABLE kerberos_db (id integer, name text, password text, key text)''')

#Insert row of database
cur.execute('''INSERT INTO kerberos_db VALUES (0,"Supragya Raj", "AEFF342234A", "AEEWQ")''')

connection.commit()

connection.close()
