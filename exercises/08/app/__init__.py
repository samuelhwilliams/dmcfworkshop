import os

from flask import Flask
from flask_bootstrap import Bootstrap

from .main import main as main_blueprint
from .misc import misc as misc_blueprint
from .nav import nav


def create_app():
    app = Flask(__name__)

    app.jinja_options = dict(app.jinja_options)
    app.jinja_options['cache_size'] = 0

    Bootstrap(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(misc_blueprint)

    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['SECRET_KEY'] = os.urandom(16).hex()

    nav.init_app(app)

    return app
