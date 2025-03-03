from flask import Flask, render_template
from .quote import Quotes

app = Flask(__name__)
q = Quotes()
q.random()

@app.route('/')
def index():
    return render_template('index.html', quote=q.random())
