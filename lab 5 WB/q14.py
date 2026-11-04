import csv
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_web_db"
)

cursor = connection.cursor()

data = []

with open("users.csv", "r") as file:

    csv_reader = csv.reader(file)

    next(csv_reader)

    for row in csv_reader:
        data.append(
            (row[0], row[1], int(row[2]))
        )

sql = """
INSERT INTO users (name, email, age)
VALUES (%s, %s, %s)
"""

cursor.executemany(sql, data)

connection.commit()

print("CSV data inserted successfully.")

cursor.close()
connection.close()