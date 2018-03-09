import json
import os

from flask import Flask

from .database import db
from .main import main as main_blueprint


def create_app():
    app = Flask(__name__)

    vcap_services = json.loads(os.getenv('VCAP_SERVICES', '{}'))
    database_uri = vcap_services.get('postgres', [{}])[0].get('credentials', {}).get('uri', 'sqlite:////tmp/no.db')
    if not database_uri.startswith('postgres'):
        print("Not connected to postgres database. What do I do!? I guess I'll just die.")
        import sys
        sys.exit(1)  # don't just remove me, fix the problem! >_> (and no the problem isn't this contrived condition)

    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(main_blueprint)

    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.config['SECRET_KEY'] = os.urandom(16).hex()

    return app
