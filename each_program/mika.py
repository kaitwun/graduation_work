# # splite3をimportする
# import sqlite3
# # flaskをimportしてflaskを使えるようにする
# from flask import Flask , render_template , request , redirect , session, url_for, Blueprint

# #Blueprintオブジェクトを生成
# app = Blueprint('mika' , __name__)

# @app.route("/level1", ["GET"])
# def level1():
#     conn = sqlite3.connect("graduation_work.db")
# <<<<<<< HEAD
#     c = conn.cursor()
# =======
#     c = conn.cursor()
#     c.execute("select id, image, title from posts where main_evaluation = level 1")
#     post = []
#     for item in c.fetchall():
#         post.append({"post_id":item[0],"image":item[1],"title":item[2]})
# >>>>>>> 95bca05df9eb8345f704e54576c47f80e50604e9
