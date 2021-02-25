# sqlite3をimport
import sqlite3
# flaskをimportする
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "sunabakoza"

