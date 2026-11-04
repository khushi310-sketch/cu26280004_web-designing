import json
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_web_db"
)

cursor = connection.cursor(
    dictionary=True
)

cursor.execute("SELECT * FROM users")

users = cursor.fetchall()

print("Content-Type: application/json")
print()

print(json.dumps(users))

cursor.close()
connection.close()