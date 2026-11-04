import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_web_db"
)

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM users")

total_users = cursor.fetchone()[0]

cursor.execute("SELECT AVG(age) FROM users")

average_age = cursor.fetchone()[0]

print("===== ADMIN REPORT =====")

print("Total Users:", total_users)

print(
    "Average Age:",
    round(average_age, 2)
    if average_age else 0
)

cursor.close()
connection.close()