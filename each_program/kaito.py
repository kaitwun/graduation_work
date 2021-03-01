# splite3をimportする
import sqlite3
# flaskをimportしてflaskを使えるようにする
from flask import Flask , render_template , request , redirect , session
# datetimeモジュールを追加
import datetime
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
# appにFlaskを定義して使えるようにしています。Flask クラスのインスタンスを作って、 app という変数に代入しています。
app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabakoza'


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        if 'user_id' in session :
            return redirect ('/top')
        else:
            return render_template("register.html")
    else:
        mail = request.form.get("e-mail")
        name = request.form.get("name")
        password = request.form.get("password")
        gender = request.form.get("gender")
        age = request.form.get("age")


        conn = sqlite3.connect('graduation_work.db')
        c = conn.cursor()
        c.execute("insert into users values(null,?,?,?,?,?)", (name, mail, password, age, gender))
        conn.commit()
        conn.close()
        return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if 'user_id' in session:
            return redirect("/")
        else:
            return render_template("login.html")
    else:
        mail = request.form.get("e-mail")
        password = request.form.get("password")
        



if __name__ == "__main__":
    app.run(debug=True)