import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/aboutus')
def index():
    return render_template('about.html')

"""
@app.route('/services')
def index():
    return render_template('services.html')

@app.route('/leantraining')
def index():
   return render_template('leantraining.html')

@app.route('/contact')
def index():
   return render_template('contact.html')

@app.route('/help')
def index():
   return render_template('help.html')

@app.route('/login')
def index():
   return render_template('login.html')
"""
