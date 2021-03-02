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
    return render_template('top.html')


@app.route("/top" ,methods=["GET"])
def top():
    conn = sqlite3.connect("graduation_work copy.db") #DBに接続
    c = conn.cursor() #DBの中身をみれるようにする
    c.execute("select image, title from posts")
    #取得した値を変数に代入
    post = []
    for item in c.fetchall(): #すべてのデータを辞書型に整形
        post.append({"image":item[0],"title":item[1]})

    # image = c.fetchall()#全部取って参る
    c.close() #DB接続終了
    print(post) #ターミナル上で確認
    #DBからimageのデータを取得
    return render_template("top.html",tpl_post = post)





if __name__ == "__main__":
    app.run(debug=True)