from flask import Blueprint, request
from models.conversation import Conversation
from models.conversation_history import ConversationHistory
from models.user import User

"""
 Defines the /conversation route for creating a new conversation.
 It receives the question, answer, summary, provider ID, and user ID from the token. 
 It creates a new conversation record and stores the conversation history.
 
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
