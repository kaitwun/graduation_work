# flaskをimportしてflaskを使えるようにする
from flask import Flask, request, render_template, redirect, session, url_for, Blueprint 
import sqlite3
import datetime
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")

# app Flaskを定義して使えるようにします。
# flaskクラスのインスタンスを使ってappという変数に代入している
app = Blueprint('takenoko' ,__name__)
# app = Flask(__name__)
@app.route("/post" ,methods = ["GET","POST"])
def new_post():
    if request.method == "get":
        if "user_id" in session:
            return render_template("post.html")
        else:
            return render_template("login.html")

    else:
        name =  request.form.get("name")
        password =  request.form.get("password")
        user_id =  request.form.get("user_id")
        title =  request.form.get("title")
        food =  request.form.get("food")
        image =  request.form.get("image")
        main_evalution=  request.form.get("main_evalution")
        main_comment =  request.form.get("main_comment")
        location =  request.form.get("location")
        category =  request.form.get("category")
        date =  request.form.get("date")
        conn = sqlite3.connect("graduation_work.db")
        c = conn.cursor()
        c.execute("INSERT INTO posts values(null,?,?,?,?,?,?,?,?,?,)",(user_id, title, food, image, main_evaluation, main_comment, location, category, date))
        conn.commit()
        conn.close()
        return render_template("intoduce.html")


@app.route("/introduce/<int:post_id>", methods =["GET","POST"])
def intoduce(post_id):
        conn = sqlite3.connect("graduation_work.db")
        c = conn.cursor()
        c.execute("SELECT user_id,title,image,main_evaluation,main_comment,location,category,date from posts WHERE post_id = ?",(post_id,))
        details = c.fetchone()
        c.execute("SELECT name FROM users WHERE id = ?",(details[0],))
        user_name = c.fetchone() 
        conn.close()
        return render_template("introduce.html" , tpl_details = details, tpl_user_name = user_name)

        if request.method == "POST":
            if "user_id" in session:
                user_id = session["user_id"]
                comment = request.form.get("comment")
                time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
                conn = sqlite3.connect("graduation_work.db")
                c = conn.cursor()
                c.execute("INSERT INTO replys values (null,?,?,?,?)"(post_id,user_id,comment,time,))
                conn.commit()
                conn.close()
                return render_template("introduce.html")

        else:
            conn = sqlite3.connect("graduation_work.db")
            c = conn.cursor()
            c.execute("SELECT users_id, others_comment, date FROM replys WHERE posts_id = ?",(post_id,))
            reply_info = c.fetchone()
            return render_template("introduce.html" reply_info = reply_info)


        




        


if __name__ == "__main__":
    app.run(debug=True)