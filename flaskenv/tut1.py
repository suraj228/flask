from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
  return "This is: <h1>HOME PAGE<h1>"

@app.route("/<userName>")
def user(userName):
  return f"hello {userName}!! welcome"

@app.route("/restricted")
def restricted():
  return redirect(url_for("home"))

if __name__ == "__main__":
  app.run()