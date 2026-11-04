import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = connection.cursor()
    cursor.execute("SELECT VERSION()")

    version = cursor.fetchone()

    print("MySQL Server Version:", version[0])

except mysql.connector.Error as error:
    print("Error:", error)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()