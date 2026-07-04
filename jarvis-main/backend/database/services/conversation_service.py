from backend.database.repositories.conversation_repository import (
    ConversationRepository,
)

class ConversationService:

    def __init__(self):

        self.repo = ConversationRepository()

    def save_user(self, conversation_id, text):

        self.repo.add_message(
            conversation_id,
            "user",
            text,
        )

    def save_assistant(self, conversation_id, text):

        self.repo.add_message(
            conversation_id,
            "assistant",
            text,
        )

    def history(self, conversation_id):

        response = self.repo.get_messages(
            conversation_id
        )

        return response.data