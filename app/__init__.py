from flask import Flask, jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return '404'


@app.route('/api/call', methods=['GET'])
def get_call():
    number = request.args.get('number', None)

    from app.controller import get_list
    list_for_return = get_list(number)

    return jsonify({'data': list_for_return})
