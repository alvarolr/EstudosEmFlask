from estudo import app
from flask import render_template

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/segundapagina/')
def segundapagina():
    return render_template('segundapagina.html')


