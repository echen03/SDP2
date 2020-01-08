import sqlite3   #enable control of an sqlite database

DB_FILE = "data.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

command = "DROP TABLE IF EXISTS users;" # delete table
c.execute(command)

<<<<<<< HEAD
command = "CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT, password TEXT, funds REAL, streak INTEGER);" # create table
=======
command = "CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT, password TEXT, funds INTEGER, streak INTEGER, card INTEGER);" # create table
>>>>>>> 35168c0e10d8132b54c9b5d13a7258c11c83b869
c.execute(command)    # run SQL statement

db.commit()
db.close()
