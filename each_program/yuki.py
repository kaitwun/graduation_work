# # flaskをimportしてflaskを使えるようにする
from flask import *
import sqlite3

# # app Flaskを定義して使えるようにします。
# # flaskクラスのインスタンスを使ってappという変数に代入している
app = Flask(__name__)


@app.route("/top")
def top():
    
    conn = sqlite3.connect("graduation_work.db") #DBに接続
    c = conn.cursor() #DBの中身をみれるようにする
    c.execute("select image from posts")
    image = c.fetchall()
    image = image[0]
    py_image = 
        return render_template("top.html",html_image)



@app.route("/introduce")
def tpl():
    return render_template("introduce.html")


if __name__ == "__main__":
    app.run(debug=True)