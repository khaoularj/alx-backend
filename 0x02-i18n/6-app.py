#!/usr/bin/env python3
"""setting up a basic flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou",
        "locale": "fr",
        "locale": "fr",
        "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def Hello():
    """this is the home page"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """function that determine the best
    match with our supported languages"""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale

    user = g.get('user')
    if user and user.get('locale') in Config.LANGUAGES:
        return user.get('locale')
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    """function that returns a user dictionary"""
    user_id = request.args.get('login_as')
    if user_id and user_id in users:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """function that stores user infos"""
    g.user = get_user()


if __name__ == '__main__':
    app.run()
