import os

from flask import Flask
from flask_bootstrap import Bootstrap

from .main import main as main_blueprint
from .nav import nav


def create_app():
    app = Flask(__name__)

    Bootstrap(app)

    app.register_blueprint(main_blueprint)

    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['SECRET_KEY'] = os.urandom(16).hex()

    nav.init_app(app)

    return app
