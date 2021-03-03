# flaskをimportしてflaskを使えるようにする
from flask import Flask, render_template
import sqlite3

# app Flaskを定義して使えるようにします。
# flaskクラスのインスタンスを使ってappという変数に代入している
app = Flask(__name__)

@app.route('/')
def new_post():
    return "New"

@app.route("/top")
def top():
    return "New POST（投稿）"



@app.route("/introduce")
def tpl():
    return render_template("introduce.html")


if __name__ == "__main__":
    app.run(debug=True)