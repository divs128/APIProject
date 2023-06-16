from flask import Blueprint, request
from models.conversation import Conversation

"""
Updates the summary of a conversation.

URL: /summary
Method: PUT

Request Body:
{
  "conversation_id": "The ID of the conversation",
  "summary": "The updated summary"
}

Response Body (on successful update):
{
  "status": "Summary updated successfully"
}

Response Body (when conversation not found):
{
  "message": "Conversation not found"
}

Response Status:
- 200: Summary updated successfully
- 404: Conversation not found

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
