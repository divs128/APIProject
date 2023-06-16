from flask import Blueprint, request
from models.user_provider import UserProvider
from models.provider import Provider
from models.address import Address
from models.provider_address import ProviderAddress
from models.user import User

"""
Retrieves user-provider details.

URL: /userprovider
Method: GET

Request Headers:
- Authorization: The user's access token

Response Body (on successful retrieval):
{
  "provider_id": "The ID of the provider",
  "provider_name": "The name of the provider",
  "speciality": "The specialty of the provider",
  "image_url": "The URL of the provider's image",
  "street1": "The first line of the provider's address",
  "street2": "The second line of the provider's address",
  "city": "The city of the provider's address",
  "zip": "The ZIP code of the provider's address"
}

Response Body (when user provider not found):
{
  "message": "User provider not found"
}

Response Body (when provider not found):
{
  "message": "Provider not found"
}

Response Body (when address not found):
{
  "message": "Address not found"
}

Response Body (when provider address not found):
{
  "message": "Provider address not found"
}

Response Status:
- 200: User-provider details retrieved successfully
- 404: User provider not found, Provider not found, Address not found, or Provider address not found

"""

userprovider_bp = Blueprint('userprovider', __name__)


@userprovider_bp.route('/userprovider', methods=['GET'])
def get_user_provider():
    user_id = User.decode_token(request.headers.get('Authorization'))

    user_provider = UserProvider.get_user_provider_by_user_id(user_id)
    if not user_provider:
        return {'message': 'User provider not found'}, 404

    provider = Provider.get_provider_by_id(user_provider.provider_id)
    if not provider:
        return {'message': 'Provider not found'}, 404

    address = Address.get_address_by_id(provider.id)
    if not address:
        return {'message': 'Address not found'}, 404

    provider_address = ProviderAddress.get_provider_address_by_provider_id(provider.id)
    if not provider_address:
        return {'message': 'Provider address not found'}, 404

    response = {
        'provider_id': provider.id,
        'provider_name': provider.name,
        'speciality': 'pcp',
        'image_url': '',
        'street1': address.street1,
        'street2': address.street2,
        'city': address.city,
        'zip': address.zip
    }

    return response, 200
