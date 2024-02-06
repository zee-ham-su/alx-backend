#!/usr/bin/env python3
"""Basic Flask-babel app"""

import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from pytz import timezone
import pytz.exceptions
from datetime import datetime


class Config(object):
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed."""
    id_login = request.args.get('login_as')
    if id_login:
        return users.get(int(id_login))
    else:
        return None


@app.before_request
def before_request():
    """Use get_user to find a user if any, and set it as a global on flask.g.user"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """The best match with our supported languages."""
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """
    Select and return appropriate timezone
    """
    time_zone = request.args.get('timezone', None)
    if time_zone:
        try:
            return timezone(time_zone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            time_zone = g.user.get('timezone')
            return timezone(time_zone)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    default_time = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_time


def get_current_time() -> str:
    """Get the current time in the user's timezone."""
    user_timezone = get_timezone()
    if user_timezone:
        current_time = datetime.now(user_timezone)
        return current_time.strftime('%b %d, %Y %I:%M:%S %p')
    else:
        return "Timezone not available"


@app.route('/')
def index() -> str:
    """Main route"""
    current_time = get_current_time()
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
