import subprocess

command = [
    "mysqldump",
    "-u", "root",
    "python_web_db"
]

with open("backup.sql", "w") as file:

    subprocess.run(
        command,
        stdout=file,
        check=True
    )

print("Database backup created successfully.")