from database.database import cursor
import jwt
from datetime import datetime, timedelta
"""
Represents a user and provides methods for user authentication and token handling.

Attributes:
- id: The ID of the user
- first_name: The first name of the user
- last_name: The last name of the user
- email: The email address of the user
- password: The password of the user

Methods:
- login(email, password): Authenticates the user with the provided email and password
- generate_token(user_id): Generates a JWT token for the given user ID
- decode_token(token): Decodes and verifies the JWT token, and retrieves the user ID

"""

class User:
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    @staticmethod
    def login(email, password):
        """
        Authenticates the user with the provided email and password.

        Parameters:
        - email: The email address of the user
        - password: The password of the user

        Returns:
        - The JWT token if authentication is successful, None otherwise
        """
        query = "SELECT id FROM user WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        if result:
            user_id = result[0]
            token = User.generate_token(user_id)
            return token
        return None

    @staticmethod
    def generate_token(user_id):
        """
        Generates a JWT token for the given user ID.

        Parameters:
        - user_id: The ID of the user

        Returns:
        - The JWT token
        """
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        token = jwt.encode(payload, 'abc123', algorithm='HS256')
        return token

    @staticmethod
    def decode_token(token):
        """
        Decodes and verifies the JWT token, and retrieves the user ID.

        Parameters:
        - token: The JWT token

        Returns:
        - The user ID if the token is valid, or an error message if the token is expired or invalid
        """
        try:
            payload = jwt.decode(token, 'abc123', algorithms=['HS256'])
            user_id = payload['sub']
            return user_id
        except jwt.ExpiredSignatureError:
            return 'Token has expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
