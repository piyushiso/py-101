import mysql.connector as con

connection = con.connect(host='localhost', user='root', password='', database='users')

if not connection.is_connected():
    print("CAN NOT CONNECT TO THE DATABASE")
    exit(0)

cursor = connection.cursor()

sql = "INSERT INTO accounts(username, password) VALUES(%s, %s)"
val = ("XYZ", "...")

cursor.execute(sql, val)

# cursor.execute("INSERT INTO accounts (username, password) VALUES('Data', '...')")
connection.commit()

print(cursor.rowcount, " rows affected.")

cursor.close()

connection.close()