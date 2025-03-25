import mysql.connector

dataBase = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd = 'redpots1'
)

# prepare cursor object
cursorObject = dataBase.cursor()

# create db
cursorObject.execute("CREATE DATABASE gard")

print("You good, fam!")