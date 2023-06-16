from database.database import cursor, conn

"""
Represents the conversation table and provides methods for creating new conversations and retrieving conversation details.

Attributes:
- id: The ID of the conversation
- user_id: The ID of the user associated with the conversation
- provider_id: The ID of the provider associated with the conversation
- summary: The summary of the conversation
- created_on: The timestamp indicating when the conversation was created
- status: The status of the conversation

Methods:
- create_conversation(question, answer, summary, provider_id, user_id): Creates a new conversation record in the database
- get_conversation_by_id(conversation_id): Retrieves a conversation object by its ID from the database

"""


class Conversation:
    def __init__(self, id, user_id, provider_id, summary, created_on, status):
        self.id = id
        self.user_id = user_id
        self.provider_id = provider_id
        self.summary = summary
        self.created_on = created_on
        self.status = status

    @staticmethod
    def create_conversation(question, answer, summary, provider_id, user_id):
         """
        Creates a new conversation record in the database.

        Parameters:
        - question: The question associated with the conversation
        - answer: The answer associated with the conversation
        - summary: The summary of the conversation
        - provider_id: The ID of the provider associated with the conversation
        - user_id: The ID of the user associated with the conversation

        Returns:
        - The ID of the created conversation
        """
        try:
            conn.start_transaction()

            # Insert conversation record
            query = "INSERT INTO conversation (user_id, provider_id, summary, created_on, status) VALUES (%s, %s, %s, " \
                    "NOW(), 'Active')"
            cursor.execute(query, (user_id, provider_id, summary))
            conversation_id = cursor.lastrowid

            # Insert conversation history
            query = "INSERT INTO conversationhistory (conversation_id, question, answer, created_on) VALUES (%s, %s, " \
                    "%s, NOW())"
            cursor.execute(query, (conversation_id, question, answer))

            conn.commit()
            return conversation_id
        except Exception as e:
            conn.rollback()
            raise e

    @staticmethod
    def get_conversation_by_id(conversation_id):
        """
        Retrieves a conversation object by its ID from the database.

        Parameters:
        - conversation_id: The ID of the conversation to retrieve

        Returns:
        - A Conversation object if the conversation is found, None otherwise
        """
        query = "SELECT id, user_id, provider_id, summary, created_on, status FROM conversation WHERE id = %s"
        cursor.execute(query, (conversation_id,))
        result = cursor.fetchone()

        if result:
            id, userid, provider_id, summary, created_on, status = result
            return Conversation(id, userid, provider_id, summary, created_on, status)
        return None
