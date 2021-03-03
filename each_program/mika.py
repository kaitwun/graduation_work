# splite3をimportする
import sqlite3
# flaskをimportしてflaskを使えるようにする
from flask import Flask , render_template , request , redirect , session, url_for, Blueprint

#Blueprintオブジェクトを生成
app = Blueprint('mika' , __name__)

#@app.route('mika')
#def new_post():    
    #return render_template "base.html