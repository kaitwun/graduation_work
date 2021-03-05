# splite3をimportする
import sqlite3
# flaskをimportしてflaskを使えるようにする
from flask import Flask , render_template , request , redirect , session, url_for, Blueprint
# datetimeモジュールを追加
import datetime
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")
# appにFlaskを定義して使えるようにしています。Flask クラスのインスタンスを作って、 app という変数に代入しています。
# Blueprintオブジェクトを生成
app = Blueprint('kaito', __name__)

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


        conn = sqlite3.connect("graduation_work.db")
        c = conn.cursor()
        c.execute("insert into users values(null,?,?,?,?,?)", (name, age, gender, mail, password))
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
        # ブラウザから送られてきた name ,password を userテーブルに一致するレコードが
        # 存在するかを判定する。レコードが存在するとuser_idに整数が代入、存在しなければ nullが入る
        conn = sqlite3.connect('graduation_work.db')
        c = conn.cursor()
        c.execute("select id from users where email = ? and password = ?", (mail, password) )
        user_id = c.fetchone()
        conn.close()
        # user_id が NULL(PythonではNone)じゃなければログイン成功
        if user_id is None:
            # ログイン失敗すると、ログイン画面に戻す
            return render_template("login.html")
        else:
            session['user_id'] = user_id[0]
            return redirect("/top")

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect("/top")

@app.route("/mypage")
def mypage():
    if request.method == "GET":
        if "user_id" in session:
            user_id = session['user_id']
            conn = sqlite3.connect('graduation_work.db')
            c = conn.cursor()
            c.execute("select name from users where id = ?", (user_id,))
            user_name = c.fetchone()
            return render_template("mypage.html", user_name = user_name)

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "GET":
        if "user_id" in session:
            user_id = session['user_id']
            conn = sqlite3.connect('graduation_work.db')
            c = conn.cursor()
            c.execute("select name, email, password, age, gender from users where id = ?", (user_id,))
            user_info = c.fetchone()
            return render_template("profile.html", user_info = user_info)

        



