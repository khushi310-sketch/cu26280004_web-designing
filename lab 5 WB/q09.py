import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_web_db"
    )

    cursor = connection.cursor()

    user_id = 3

    sql = "DELETE FROM users WHERE id = %s"

    cursor.execute(sql, (user_id,))

    connection.commit()

    print("Record deleted successfully.")

except mysql.connector.Error as error:

    print("Database Error:", error)

finally:

    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()