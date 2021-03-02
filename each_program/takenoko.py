# flaskをimportしてflaskを使えるようにする
from flask import Flask, request, render_template, redirect, session, url_for, Blueprint 
import sqlite3

# app Flaskを定義して使えるようにします。
# flaskクラスのインスタンスを使ってappという変数に代入している
app = Blueprint('takenoko' ,__name__)
# app = Flask(__name__)
@app.route("/post" ,methods = ["get","post"])
def new_post():
    if request.method == "get":
        if "user_id" in session:
            return redirect("/post")
        else:
            return render_template("login.html")

    else:
        name =  request.form.get("name")
        password =  request.form.get("password")
        conn = sqlite3.connect("gradueathon_works.db")
        c = conn.cursor()
        c.execute("INSERT INTO posts values(user_id, title, food, images, main_evalution, main_comment, location, category, date)")
        conn.commit()
        conn.close()
        return render_template("/intoduce")


            
    




