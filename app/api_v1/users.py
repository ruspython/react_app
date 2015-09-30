from flask import jsonify, request

from . import api
from .. import db
from ..models.users import User
from ..schemas.users import user_schema, user_schema


@api.route('/users', methods=['GET'])
def get_users():
    return jsonify({'user1': 'man'})


@api.route('/users/<int:id>', methods=['GET'])
def get_users(id):
    pass


@api.route('/users', methods=['POST'])
def create_users():
    pass


@api.route('/users/<int:id>', methods=['PUT'])
def update_users(id):
    pass


@api.route('/users/<int:id>', methods=['DELETE'])
def delete_users(id):
    pass
