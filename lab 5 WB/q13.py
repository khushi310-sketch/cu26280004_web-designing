import logging
import mysql.connector

logging.basicConfig(
    filename="server.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_web_db"
    )

    print("Database connected successfully.")

except mysql.connector.Error as error:

    logging.error(f"Database Error: {error}")

    print("Error logged successfully.")