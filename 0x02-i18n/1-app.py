#!/usr/bin/env python3
"""setting up a basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def Hello():
    """this is the home page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
