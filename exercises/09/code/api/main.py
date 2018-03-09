from flask import jsonify, abort
from flask.blueprints import Blueprint

from .database import db
from .models import User


main = Blueprint('main', __name__)


@main.route('/')
def home():
    return jsonify({"status": "ok"})


@main.route('/users')
def users():
    return jsonify({'users': [user.serialize() for user in User.query.all()]})


@main.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)

    return jsonify({'user': user.serialize()})


@main.route('/users/<string:username>')
def get_user_by_username(username):
    return jsonify({'user': User.query.filter(User.username == username).first_or_404().serialize()})


@main.route('/_status')
def status():
    return jsonify({"status": "ok"})
