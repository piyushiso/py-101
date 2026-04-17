# pip install mysql-connector-python

import mysql.connector

connection = mysql.connector.connect("localhost", "root", "", "users")

if not connection.is_connected():
    print("ERROR CONNECTING TO THE DATABASE")
    quit()
    
cusor = connection.cursor()

cusor.execute("SELECT * FROM accounts")

print(cusor.fetchall())