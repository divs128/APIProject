from database.database import cursor, conn
"""
Represents the conversationhistory table and provides methods for storing conversation history.
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
        try:
            query = "INSERT INTO conversationhistory (conversation_id, question, answer, created_on) VALUES (%s, %s, " \
                    "%s, NOW())"
            cursor.execute(query, (conversation_id, question, answer))
            return cursor.lastrowid
        except Exception as e:
            conn.rollback()
            raise e
