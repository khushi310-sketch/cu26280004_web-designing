import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_web_db"
)

cursor = connection.cursor()

sql = """
INSERT INTO users (name, email, age)
VALUES (%s, %s, %s)
"""

users = [
    ("Khushi", "khushi@gmail.com", 21),
    ("Rahul", "rahul@gmail.com", 22),
    ("Aman", "aman@gmail.com", 20)
]

cursor.executemany(sql, users)

connection.commit()

print(cursor.rowcount, "records inserted successfully.")

cursor.close()
connection.close()