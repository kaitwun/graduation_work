# # flaskをimportしてflaskを使えるようにする
from flask import *
import sqlite3

# # app Flaskを定義して使えるようにします。
# # flaskクラスのインスタンスを使ってappという変数に代入している
app = Flask(__name__)


@app.route("/top")
def top():
    return render_template("top.html")


@app.route("/introduce")
def tpl():
    return render_template("introduce.html")


if __name__ == "__main__":
    app.run(debug=True)