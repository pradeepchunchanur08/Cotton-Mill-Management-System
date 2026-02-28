from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary login data (You will connect to MySQL later)
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

@app.route("/")
def home():
    return render_template("admin_login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return "Login Successful!"
    else:
        return "Invalid Username or Password"

if __name__ == "__main__":
    app.run(debug=True)