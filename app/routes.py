from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    todos = [
        {
            'text':'eat',
            'completed': False
        },
        {
            'text': 'sleep',
            'completed': False
        },
        {
            'text': 'code',
            'completed': False
        }
    ]
    return render_template('index.html', todos=todos)