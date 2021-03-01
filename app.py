import each_program
from flask import Flask, render_template, request, redirect, session
import sqlite3
import datetime
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
app = Flask(__name__)
app.secret_key = "sunabacokoza"


if __name__ == "__main__":
    app.run(debug=True)