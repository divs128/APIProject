from database.database import cursor

"""
Represents the userprovider table and provides methods for
retrieving the user-provider relationship

"""


class UserProvider:
    def __init__(self, id, user_id, provider_id):
        self.id = id
        self.user_id = user_id
        self.provider_id = provider_id

    @staticmethod
    def get_user_provider_by_user_id(user_id):
        query = "SELECT id, user_id, provider_id FROM userprovider WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()

        if result:
            id, user_id, provider_id = result
            return UserProvider(id, user_id, provider_id)
        return None
