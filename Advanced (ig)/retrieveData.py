import mysql.connector as C

con = C.connect(host = 'localhost', user='root', password='', database='users')

cursor = con.cursor()

sql = "SELECT * FROM accounts"
cursor.execute(sql)

while True:
    data = cursor.fetchone()
    if(data is None):
        break
    print(data)
