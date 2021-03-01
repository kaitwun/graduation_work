import each_program
from flask import Flask, render_template, request, redirect, session, url_for
from each_program import kaito, mika, takenoko, yuki
import sqlite3
import datetime
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
app = Flask(__name__)
app.secret_key = "sunabacokoza"

app.register_blueprint(kaito.app)


if __name__ == "__main__":
    app.run(debug=True)