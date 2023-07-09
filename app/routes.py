from app import app

from flask import render_template

@app.route('/')
def land():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/team')
def team():
    return render_template('team.html')

