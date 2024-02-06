#!/usr/bin/env python3
'''flask 5-app.py'''
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)


class Config:
    '''config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


def get_user():
    '''get_user method'''
    id = request.args.get('login_as')
    if id:
        return users.get(int(id), None)


@app.before_request
def before_request():
    '''before_request methode'''
    g.user = get_user()


@babel.localeselector
def get_locale():
    '''get_local method'''
    lang = request.args.get('locale')
    supported = app.config['LANGUAGES']
    if lang in supported:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''index page of the app'''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
