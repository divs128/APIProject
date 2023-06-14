from flask import Blueprint, request
from models.user_provider import UserProvider
from models.provider import Provider
from models.address import Address
from models.provider_address import ProviderAddress
from models.user import User

"""
Defines the /userprovider route for retrieving user-provider details. 
It requires a token for authentication, decodes the token, 
and fetches the corresponding user-provider information from the database
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
