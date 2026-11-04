import mysql.connector
from mysql.connector import pooling

connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host="localhost",
    user="root",
    password="",
    database="python_web_db"
)

connection = connection_pool.get_connection()

cursor = connection.cursor()

cursor.execute("SELECT * FROM users")

records = cursor.fetchall()

for record in records:
    print(record)

cursor.close()
connection.close()