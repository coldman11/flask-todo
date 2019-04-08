from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    todos = ['elo', 'siema', 'cze']
    return render_template('index.html', todos=todos)