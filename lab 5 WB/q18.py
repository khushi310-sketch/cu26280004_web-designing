from flask import Flask, session

app = Flask(__name__)

app.secret_key = "change_this_to_a_strong_random_secret"


@app.route("/login")
def login():

    session["username"] = "Khushi"

    return "Login successful!"


@app.route("/profile")
def profile():

    if "username" in session:
        return "Welcome " + session["username"]

    return "Please login first."


@app.route("/logout")
def logout():

    session.pop("username", None)

    return "Logged out successfully."


if __name__ == "__main__":
    app.run(debug=True)