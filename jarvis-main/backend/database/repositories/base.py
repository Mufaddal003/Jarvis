from backend.database.client import Database

class BaseRepository:

    table = ""

    def __init__(self):

        self.db = Database.client()

    def all(self):

        return (
            self.db.table(self.table)
            .select("*")
            .execute()
        )

    def insert(self, data):

        return (
            self.db.table(self.table)
            .insert(data)
            .execute()
        )

    def update(self, record_id, data):

        return (
            self.db.table(self.table)
            .update(data)
            .eq("id", record_id)
            .execute()
        )

    def delete(self, record_id):

        return (
            self.db.table(self.table)
            .delete()
            .eq("id", record_id)
            .execute()
        )