#!/usr/bin/env python3
"""setting up a basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """function that determine the best
    match with our supported languages"""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def Hello():
    """this is the home page"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
