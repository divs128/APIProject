from database.database import cursor
"""
Represents the address table and provides methods for retrieving address details.

Attributes:
- id: The ID of the address
- street1: The first line of the address
- street2: The second line of the address
- city: The city of the address
- zip: The ZIP code of the address

Methods:
- get_address_by_id(address_id): Retrieves an address object by its ID from the database

"""
class Address:
    def __init__(self, id, street1, street2, city, zip):
        self.id = id
        self.street1 = street1
        self.street2 = street2
        self.city = city
        self.zip = zip

    @staticmethod
    def get_address_by_id(address_id):
         """
        Retrieves an address object by its ID from the database.

        Parameters:
        - address_id: The ID of the address to retrieve

        Returns:
        - An Address object if the address is found, None otherwise
        """

        query = "SELECT id, street1, street2, city, zip FROM address WHERE id = %s"
        cursor.execute(query, (address_id,))
        result = cursor.fetchone()

        if result:
            id, street1, street2, city, zip = result
            return Address(id, street1, street2, city, zip)
        return None
