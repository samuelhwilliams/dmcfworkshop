from flask import render_template, jsonify
from flask.blueprints import Blueprint
from flask_nav.elements import Navbar, View

from .nav import nav


main = Blueprint('main', __name__)

nav.register_element('main_top',
                     Navbar(View('Home', '.home'), )
                     )


@main.route('/')
def home():
    # time.sleep(20)
    return render_template('home.html')


@main.route('/version')
def version():
    return jsonify({'version': 2})
