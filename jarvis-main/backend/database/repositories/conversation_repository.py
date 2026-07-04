from .base import BaseRepository

class ConversationRepository(BaseRepository):

    table = "conversations"

    def get_messages(self, conversation_id):

        return (
            self.db.table("messages")
            .select("*")
            .eq("conversation_id", conversation_id)
            .order("created_at")
            .execute()
        )

    def add_message(
        self,
        conversation_id,
        role,
        content,
        tokens=0,
    ):

        return (
            self.db.table("messages")
            .insert(
                {
                    "conversation_id": conversation_id,
                    "role": role,
                    "content": content,
                    "token_count": tokens,
                }
            )
            .execute()
        )