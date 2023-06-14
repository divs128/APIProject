from flask import Blueprint, request
from models.conversation import Conversation

"""
Defines the /summary route for updating the summary of a conversation. 
It receives the conversation ID and the updated summary, and 
updates the conversation record in the database

"""
summary_bp = Blueprint('summary', __name__)
@summary_bp.route('/summary', methods=['PUT'])


def update_summary():
    conversation_id = request.json.get('conversation_id')
    summary = request.json.get('summary')

    conversation = Conversation.get_conversation_by_id(conversation_id)

    if conversation:
        # Update the summary
        conversation.summary = summary
        return {'status': 'Summary updated successfully'}, 200
    else:
        return {'message': 'Conversation not found'}, 404
