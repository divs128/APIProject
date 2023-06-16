from flask import Blueprint, request
from models.conversation import Conversation
from models.conversation_history import ConversationHistory
from models.user import User

"""
Creates a new conversation.

URL: /conversation
Method: POST

Request Body:
{
  "question": "The question asked by the user",
  "answer": "The answer provided by the provider",
  "summary": "The summary of the conversation",
  "provider_id": "The ID of the conversation provider",
}

Request Headers:
{
  "Authorization": "Bearer <user_token>"
}

Response Body:
{
  "conversation_id": "The ID of the created conversation"
}

Response Status:
- 201: Conversation created successfully

"""
conversation_bp = Blueprint('conversation', __name__)
@conversation_bp.route('/conversation', methods=['POST'])

def create_conversation():
    question = request.json.get('question')
    answer = request.json.get('answer')
    summary = request.json.get('summary')
    provider_id = request.json.get('provider_id')
    user_id = User.decode_token(request.headers.get('Authorization'))

    conversation_id = Conversation.create_conversation(question, answer, summary, provider_id, user_id)

    return {'conversation_id': conversation_id}, 201
