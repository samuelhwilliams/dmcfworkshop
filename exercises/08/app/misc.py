from flask import jsonify
from flask.blueprints import Blueprint


misc = Blueprint('misc', __name__)

MB = 1024 * 1024
MY_BIG_LEAK = ''


# TODO: remove me
@misc.route('/leak_memory')
def home():
    global MY_BIG_LEAK
    MY_BIG_LEAK += '1' * 8 * MB
    return jsonify({'status': 'done'})
