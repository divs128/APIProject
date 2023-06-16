from database.database import cursor, conn
"""
Represents the conversationhistory table and provides methods for storing conversation history.

Attributes:
- id: The ID of the conversation history entry
- conversation_id: The ID of the conversation associated with the history entry
- question: The question in the conversation
- answer: The answer in the conversation
- created_on: The timestamp indicating when the history entry was created

Methods:
- create_conversation_history(conversation_id, question, answer): Stores a new conversation history entry in the database

"""
class ConversationHistory:
    def __init__(self, id, conversation_id, question, answer, created_on):
        self.id = id
        self.conversation_id = conversation_id
        self.question = question
        self.answer = answer
        self.created_on = created_on

    @staticmethod
    def create_conversation_history(conversation_id, question, answer):
        """
        Stores a new conversation history entry in the database.

        Parameters:
        - conversation_id: The ID of the conversation associated with the history entry
        - question: The question in the conversation
        - answer: The answer in the conversation

        Returns:
        - The ID of the created conversation history entry
        """
        try:
            query = "INSERT INTO conversationhistory (conversation_id, question, answer, created_on) VALUES (%s, %s, " \
                    "%s, NOW())"
            cursor.execute(query, (conversation_id, question, answer))
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            raise e
