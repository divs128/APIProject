from database.database import cursor
"""
Represents the provider table and provides methods for retrieving provider details

"""
class Provider:
    def __init__(self, id, name, npi):
        self.id = id
        self.name = name
        self.npi = npi

    @staticmethod
    def get_provider_by_id(provider_id):
        query = "SELECT id, name, npi FROM provider WHERE id = %s"
        cursor.execute(query, (provider_id,))
        result = cursor.fetchone()

        if result:
            id, name, npi = result
            return Provider(id, name, npi)
        return None
