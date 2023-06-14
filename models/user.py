from database.database import cursor
import jwt
from datetime import datetime, timedelta

class User:
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    @staticmethod
    def login(email, password):
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
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        token = jwt.encode(payload, 'abc123', algorithm='HS256')
        return token

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(token, 'abc123', algorithms=['HS256'])
            user_id = payload['sub']
            return user_id
        except jwt.ExpiredSignatureError:
            return 'Token has expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
