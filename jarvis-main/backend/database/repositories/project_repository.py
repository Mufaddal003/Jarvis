from .base import BaseRepository

class ProjectRepository(BaseRepository):

    table = "projects"

    def recent(self, user_id):

        return (
            self.db.table(self.table)
            .select("*")
            .eq("user_id", user_id)
            .order("updated_at", desc=True)
            .execute()
        )