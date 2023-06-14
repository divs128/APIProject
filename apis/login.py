from flask import Blueprint, request
from models.user import User

"""
Defines the /login route for user authentication. It receives the email and password,
 verifies them against the database, and returns a token if authentication is successful
"""

login_bp = Blueprint('login', __name__)
@login_bp.route('/login', methods=['POST'])

def login():
    email = request.json.get('email')
    password = request.json.get('password')

    token = User.login(email, password)

    if token:
        return {'token': token}, 200
    else:
        return {'message': 'Invalid email or password'}, 401
