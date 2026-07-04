from .base import BaseRepository

class MemoryRepository(BaseRepository):

    table = "memories"

    def search(self, user_id):

        return (
            self.db.table(self.table)
            .select("*")
            .eq("user_id", user_id)
            .execute()
        )