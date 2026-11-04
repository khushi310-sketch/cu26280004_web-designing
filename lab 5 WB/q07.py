#!/usr/bin/env python3

import cgi
import mysql.connector

form = cgi.FieldStorage()

name = form.getvalue("name")
email = form.getvalue("email")
age = form.getvalue("age")

print("Content-Type: text/html")
print()

try:
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

    cursor.execute(sql, (name, email, age))

    connection.commit()

    print("<h2>User inserted successfully!</h2>")

except Exception as error:
    print("<h2>Error:</h2>", error)

finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()