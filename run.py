from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'todos.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)


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

if __name__ == '__main__':
    app.run(debug=True)