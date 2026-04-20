# Advised to create a virtual environment
# python -m venv db-env
# db-env\Scripts\activate
# pip install mysql-connector-python

import mysql.connector as con

connection = con.connect(host='localhost', user='root', password='', database='users')

if not connection.is_connected():
    print("ERROR CONNECTING TO THE DATABASE")
    quit()
    
cursor = connection.cursor()

cursor.execute("INSERT INTO accounts (username, password) VALUES('User', 'User')")
# sql = "INSERT INTO accounts(username, password) VALUES(%s, %s)"
# val = ("John", "Cena")
# cursor.execute(sql, val)
connection.commit()

print(cursor.rowcount, " records inserted")

# cursor.execute("SELECT * FROM accounts")

# # print(cusor.fetchall())

# while True:
#     data = cursor.fetchone()
#     if data is None:
#         break
#     print(data)