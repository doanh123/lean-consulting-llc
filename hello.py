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
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/help')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/services')
def service():
    return render_template('service.html')

@app.route('/leantraining')
def training():
    return render_template('leantraining.html')
