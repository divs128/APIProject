from database.database import cursor
"""
Represents the provider table and provides methods for retrieving provider details.

Attributes:
- id: The ID of the provider
- name: The name of the provider
- npi: The National Provider Identifier (NPI) of the provider

Methods:
- get_provider_by_id(provider_id): Retrieves a provider by ID from the database

"""
class Provider:
    def __init__(self, id, name, npi):
        self.id = id
        self.name = name
        self.npi = npi

    @staticmethod
    def get_provider_by_id(provider_id):
        """
        Retrieves a provider by ID from the database.

        Parameters:
        - provider_id: The ID of the provider

        Returns:
        - The Provider object if found, None otherwise
        """
        query = "SELECT id, name, npi FROM provider WHERE id = %s"
        cursor.execute(query, (provider_id,))
        result = cursor.fetchone()

        if result:
            id, name, npi = result
            return Provider(id, name, npi)
        return None
