from flask import Blueprint, request
from models.user import User

"""
Performs user authentication and generates a token.

URL: /login
Method: POST

Request Body:
{
  "email": "The user's email",
  "password": "The user's password"
}

Response Body (on successful authentication):
{
  "token": "The generated authentication token"
}

Response Body (on failed authentication):
{
  "message": "Invalid email or password"
}

Response Status:
- 200: Authentication successful
- 401: Invalid email or password

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
