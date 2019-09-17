from flask import Flask, render_template, make_response
from .quote import Quotes

app = Flask(__name__)
q = Quotes()

@app.route('/')
def index():
    return render_template('index.html', quote=q.random())
