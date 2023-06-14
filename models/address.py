from database.database import cursor
"""
Represents the address table and provides methods for retrieving address details
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
        query = "SELECT id, street1, street2, city, zip FROM address WHERE id = %s"
        cursor.execute(query, (address_id,))
        result = cursor.fetchone()

        if result:
            id, street1, street2, city, zip = result
            return Address(id, street1, street2, city, zip)
        return None
