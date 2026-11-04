import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_web_db"
)

cursor = connection.cursor()

name = input("Enter user name: ")

sql = "SELECT * FROM users WHERE name = %s"

cursor.execute(sql, (name,))

records = cursor.fetchall()

for row in records:
    print(row)

cursor.close()
connection.close()