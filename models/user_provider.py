from database.database import cursor
"""
Represents the user-provider relationship and provides methods for retrieving user-provider details.

Attributes:
- id: The ID of the user-provider relationship
- user_id: The ID of the user
- provider_id: The ID of the provider

Methods:
- get_user_provider_by_user_id(user_id): Retrieves the user-provider relationship for the given user ID

"""


class UserProvider:
    def __init__(self, id, user_id, provider_id):
        self.id = id
        self.user_id = user_id
        self.provider_id = provider_id

    @staticmethod
    def get_user_provider_by_user_id(user_id):
        """
        Retrieves the user-provider relationship for the given user ID.

        Parameters:
        - user_id: The ID of the user

        Returns:
        - The UserProvider object if the user-provider relationship exists, None otherwise
        """
        query = "SELECT id, user_id, provider_id FROM userprovider WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()

        if result:
            id, user_id, provider_id = result
            return UserProvider(id, user_id, provider_id)
        return None
