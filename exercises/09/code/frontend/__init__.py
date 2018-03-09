import os

from flask import Flask
from flask_bootstrap import Bootstrap

from .main import main as main_blueprint
from .nav import nav
from .login import login_manager


def create_app():
    app = Flask(__name__)

    app.config['API_URL'] = os.getenv('API_URL', 'http://invalid.url')

    login_manager.init_app(app)
    login_manager.login_view = 'main.home'
    login_manager.login_message_category = "must_login"

    Bootstrap(app)

    app.register_blueprint(main_blueprint)

    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['SECRET_KEY'] = os.urandom(16).hex()

    nav.init_app(app)

    return app
