from application.app import app
from flask import render_template


@app.route('/')
def index():
    name = 'USER'
    return render_template('index.html', n=name)
