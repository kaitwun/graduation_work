# flaskをimportしてflaskを使えるようにする
from flask import Flask, render_template, render_template, redirect, session, url_for, Blueprint 
import sqlite3

# app Flaskを定義して使えるようにします。
# flaskクラスのインスタンスを使ってappという変数に代入している
app = Blueprint('takenoko' ,__name__)
# app = Flask(__name__)
@app.route("/intoroduce")
def ():
    