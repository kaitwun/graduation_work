# # flaskをimportしてflaskを使えるようにする
from flask import Flask, render_template, request, redirect, session, url_for ,Blueprint
import sqlite3

# # app Flaskを定義して使えるようにします。
# # flaskクラスのインスタンスを使ってappという変数に代入している
app = Blueprint('yuki' ,__name__)
# app = Flask(__name__)

app.secret_key = "sunabacokoza"

@app.route("/")
def index():
    return redirect('/top')


@app.route("/top" ,methods=["GET"])
def top():
    conn = sqlite3.connect("graduation_work.db") #DBに接続
    c = conn.cursor() #DBの中身をみれるようにする
    c.execute("SELECT id, image, title from posts;")
    #取得した値を変数に代入
    post = []
    for item in c.fetchall(): #すべてのデータを辞書型に整形
        post.append({"post_id":item[0],"image":item[1],"title":item[2]})

    # image = c.fetchall()#全部取って参る
    # c.close() #DB接続終了
    print(post) #ターミナル上で確認
    # #DBからimageのデータを取得
    # return render_template("top.html",tpl_post = post)

    c.execute("SELECT id, image from posts where main_evaluation = 'level 1'")
    image_1 = c.fetchmany(3)
    # c.close()
    # print(image_1) 
    # print(image_1[0]) #要素の確認
    # return render_template("top.html",tpl_level1 = image_1)

    c.execute("SELECT  id, image from posts where main_evaluation = 'level 2'")
    image_2 = c.fetchmany(3)
    # c.close()
    # print(image_2)
    # print(image_2[0])
    # print(image_2[1])

    c.execute("SELECT id, image from posts where main_evaluation = 'level 3'")
    image_3 = c.fetchmany(3)
    c.close()
    # print(image_3)
    return render_template("top.html", tpl_post = post, tpl_level1 = image_1, tpl_level2 = image_2, tpl_level3 = image_3)
   

@app.route("/introduce/<int:post_id>")
def introduce_get(post_id):
    conn = sqlite3.connect("graduation_work.db") #DBに接続
    c = conn.cursor() #DBの中身をみれるようにする
    c.execute("select * from posts where id = ?" ,(post_id,))
    details_post = c.fetchone()
    c.close()
    # print(details_post)
    return render_template("introduce.html")


@app.route("/level1", methods=["GET"])
def level1():
    conn = sqlite3.connect("graduation_work.db")
    c = conn.cursor()
    c.execute("select id, image, title from posts where main_evaluation = 'level 1'")
    post = []
    for item in c.fetchall():
        post.append({"post_id":item[0],"image":item[1],"title":item[2]})
    return render_template("level1.html", tpl_post = post,)


@app.route("/level2", methods=["GET"])
def level2():
    conn = sqlite3.connect("graduation_work.db")
    c = conn.cursor()
    c.execute("select id, image, title from posts where main_evaluation = 'level 2'")
    post = []
    for item in c.fetchall():
        post.append({"post_id":item[0],"image":item[1],"title":item[2]})
    return render_template("level2.html", tpl_post = post,)
    

@app.route("/level3", methods=["GET"])
def level3():
    conn = sqlite3.connect("graduation_work.db")
    c = conn.cursor()
    c.execute("select id, image, title from posts where main_evaluation = 'level 3'")
    post = []
    for item in c.fetchall():
        post.append({"post_id":item[0],"image":item[1],"title":item[2]})
    return render_template("level3.html", tpl_post = post,)

if __name__ == "__main__":
    app.run(debug=True)