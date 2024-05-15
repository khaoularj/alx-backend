#!/usr/bin/env python3
"""setting up a basic flask app"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class configuration for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def Hello():
    """this is the home page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
