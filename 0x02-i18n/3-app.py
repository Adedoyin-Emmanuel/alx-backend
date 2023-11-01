#!/usr/bin/env python3
""" A basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    """ Configuration class for the application """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Fuction to determine best match
    with supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """This displays the index.html page """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
