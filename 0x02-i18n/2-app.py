#!/usr/bin/env python3
'''flask 2-app.py'''
from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__)


class Config:
    '''config class'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''get_local method'''
    return request.accept_languages.best_match(app.config[Config.LANGUAGES])


@app.route('/')
def index():
    '''index page of the app'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
