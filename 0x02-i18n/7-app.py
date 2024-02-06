import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from functools import wraps


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
    """ function that returns a user dictionary or
    None if the ID cannot be found or if login_as was not passed."""
    id_login = request.args.get('login_as')
    if id_login:
        return users.get(int(id_login))
    else:
        return None


@app.before_request
def before_request():
    """ use get_user to find a user if any,
    and set it as a global on flask.g.user"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """the best match with our supported languages."""
    lang = request.args.get('locale')
    if lang in app.config['LANGUAGES']:
        return lang

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    if best_match:
        return best_match

    return app.config['BABEL_DEFAULT_LOCALE']


def timezone_selector(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        timezone_param = request.args.get('timezone')
        if timezone_param:
            try:
                pytz.timezone(timezone_param)
                return f(*args, **kwargs)
            except pytz.exceptions.UnknownTimeZoneError:
                pass

        if g.user and g.user.get('timezone'):
            try:
                pytz.timezone(g.user.get('timezone'))
                return f(*args, **kwargs)
            except pytz.exceptions.UnknownTimeZoneError:
                pass

        return app.config['BABEL_DEFAULT_TIMEZONE']
    return decorated_function


@app.route('/')
@timezone_selector
def index() -> str:
    """Main route"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
