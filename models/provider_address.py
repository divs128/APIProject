from database.database import cursor
"""
Represents the provideraddress table and provides methods for retrieving provider-address mapping.

Attributes:
- id: The ID of the provider-address mapping
- provider_id: The ID of the provider
- address_id: The ID of the address

Methods:
- get_provider_address_by_provider_id(provider_id): Retrieves the provider-address mapping by provider ID from the database

"""
class ProviderAddress:
    def __init__(self, id, provider_id, address_id):
        self.id = id
        self.provider_id = provider_id
        self.address_id = address_id

    @staticmethod
    def get_provider_address_by_provider_id(provider_id):
        """
        Retrieves the provider-address mapping by provider ID from the database.

        Parameters:
        - provider_id: The ID of the provider

        Returns:
        - The ProviderAddress object if found, None otherwise
        """
        query = "SELECT id, provider_id, address_id FROM provideraddress WHERE provider_id = %s"
        cursor.execute(query, (provider_id,))
        result = cursor.fetchone()

        if result:
            id, provider_id, address_id = result
            return ProviderAddress(id, provider_id, address_id)
        return None
