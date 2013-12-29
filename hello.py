import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def index():
    return render_template('home.html')




