
from flask import Flask, render_template, request, redirect, session, url_for, Blueprint
from each_program import kaito, mika, takenoko, yuki

import sqlite3
import datetime
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
app = Flask(__name__)
app.secret_key = "sunabacokoza"

app.register_blueprint(kaito.app)

<<<<<<< HEAD
app.register_blueprint(mika.app)
=======
app.register_blueprint(mika.app)
>>>>>>> 2e24813faa0c8889ea0d2e7d1b7c0ff5daa19ff3
app.register_blueprint(takenoko.app)
app.register_blueprint(yuki.app)


if __name__ == "__main__":
    app.run(debug=True)