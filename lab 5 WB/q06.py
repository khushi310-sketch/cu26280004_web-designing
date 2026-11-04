import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_web_db"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM users")

records = cursor.fetchall()

html = """
<html>
<body>
<h2>User Records</h2>

<table border="1">
<tr>
<th>ID</th>
<th>Name</th>
<th>Email</th>
<th>Age</th>
</tr>
"""

for row in records:
    html += f"""
    <tr>
        <td>{row[0]}</td>
        <td>{row[1]}</td>
        <td>{row[2]}</td>
        <td>{row[3]}</td>
    </tr>
    """

html += """
</table>
</body>
</html>
"""

print(html)

cursor.close()
connection.close()