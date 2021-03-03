# # flaskをimportしてflaskを使えるようにする
from flask import Flask, render_template, request, redirect, session, url_for ,Blueprint
import sqlite3

# # app Flaskを定義して使えるようにします。
# # flaskクラスのインスタンスを使ってappという変数に代入している
app = Blueprint('yuki' ,__name__)
# app = Flask(__name__)

# app.secret_key = "sunabacokoza"

@app.route("/")
def index():
    return render_template('top.html')


@app.route("/top")
def top():
    conn = sqlite3.connect("graduation_work copy.db") #DBに接続
    c = conn.cursor() #DBの中身をみれるようにする
    c.execute("SELECT image, title from posts;")
    #取得した値を変数に代入
    post = []
    for item in c.fetchall(): #すべてのデータを辞書型に整形
        post.append({"image":item[0],"title":item[1]})

    # image = c.fetchall()#全部取って参る
    # c.close() #DB接続終了
    print(post) #ターミナル上で確認
    # #DBからimageのデータを取得
    # return render_template("top.html",tpl_post = post)

    c.execute("SELECT image from posts where main_evaluation = 'level 1'")
    image_1 = c.fetchmany(3)
    # c.close()
    print(image_1) 
    print(image_1[0]) #要素の確認
    # return render_template("top.html",tpl_level1 = image_1)

    c.execute("SELECT image from posts where main_evaluation = 'level 2'")
    image_2 = c.fetchmany(3)
    # c.close()
    print(image_2)
    print(image_2[0])
    print(image_2[1])

    c.execute("SELECT image from posts where main_evaluation = 'level 3'")
    image_3 = c.fetchmany(3)
    c.close()
    print(image_3)
    return render_template("top.html",tpl_post = post, tpl_level1 = image_1, tpl_level2 = image_2, tpl_level3 = image_3)
   

@app.route("/introduce-get/<int:post_id>")
def introduce_get(post_id):
    conn = sqlite3.connect("graduation_work.db") #DBに接続
    c = conn.cursor() #DBの中身をみれるようにする
    c.execute("select * from posts where id = ?" ,(post_id,))
    intrduce_post = c.fechone()
    c.close()
    print(into)


    return render_template("intoroduce.html"/)

if __name__ == "__main__":
    app.run(debug=True)