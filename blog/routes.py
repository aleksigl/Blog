from flask import Flask, request, render_template, redirect, url_for, jsonify
from blog import app

app.config["SECRET_KEY"] = "qwerty"


@app.route("/")
def homepage():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)

