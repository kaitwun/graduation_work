import each_program
from flask import Flask, render_template, request, redirect, session
import sqlite3
app = Flask(__name__)
app.secret_key = "sunabacokoza"

if __name__ == "__main__":
    app.run(debug=True)