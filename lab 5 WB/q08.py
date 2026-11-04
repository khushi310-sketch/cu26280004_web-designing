import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_web_db"
)

cursor = connection.cursor()

user_id = 1
new_name = "Khushi Yadav"
new_email = "khushi.yadav@gmail.com"

sql = """
UPDATE users
SET name = %s, email = %s
WHERE id = %s
"""

cursor.execute(
    sql,
    (new_name, new_email, user_id)
)

connection.commit()

print("User updated successfully.")

cursor.close()
connection.close()