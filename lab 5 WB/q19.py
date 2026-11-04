import re
import mysql.connector


def valid_name(name):
    return bool(
        re.match(
            r"^[A-Za-z ]{2,100}$",
            name
        )
    )


def valid_email(email):
    return bool(
        re.match(
            r"^[^@]+@[^@]+\.[^@]+$",
            email
        )
    )


name = input("Enter name: ").strip()
email = input("Enter email: ").strip()
age = input("Enter age: ").strip()


if not valid_name(name):
    print("Invalid name.")

elif not valid_email(email):
    print("Invalid email.")

elif not age.isdigit():
    print("Invalid age.")

else:

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

    cursor.execute(
        sql,
        (name, email, int(age))
    )

    connection.commit()

    print("Valid data inserted successfully.")

    cursor.close()
    connection.close()