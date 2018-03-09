import json

from flask import render_template, url_for, redirect, request, current_app, flash, jsonify
from flask.blueprints import Blueprint
from flask_login import login_required, login_user, logout_user
from flask_nav.elements import Navbar, View
import requests

from .forms import LoginForm
from .nav import nav
from .login import login_manager
from .user import User


main = Blueprint('main', __name__)

nav.register_element('main_top',
                     Navbar(View('Home', '.home'), )
                     )


@login_manager.user_loader
def load_user(user_id):
    res = requests.get(f'{current_app.config["API_URL"]}/users/{user_id}')
    data = json.loads(res)
    user = User(**data['user'])
    return user


@main.route('/', methods=['GET', 'POST'])
def home():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        res = requests.get(f'{current_app.config["API_URL"]}/users/{form.data["username"]}')
        if res.status_code == 200:
            data = json.loads(res)
            user = User(**data['user'])

            if form.data['password'] != user.password:
                flash('No account found with that username/password combination.', 'danger')

            elif user.active is False:
                flash('That user account has been deactivated.', 'warning')

            else:
                login_user(user)
                return redirect(url_for('.logged_in'))

        else:
            flash('No account found with that username/password combination.', 'danger')

    return render_template('home.html', form=form)


@main.route('/logged_in')
@login_required
def logged_in():
    logout_user()
    return render_template('logged_in.html')


@main.route('/_status')
def status():
    return jsonify({"status": "ok"})
