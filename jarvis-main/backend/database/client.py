import os

from dotenv import load_dotenv

from supabase import create_client, Client

load_dotenv()

class Database:

    _client = None

    @classmethod
    def client(cls) -> Client:

        if cls._client is None:

            cls._client = create_client(
                os.getenv("SUPABASE_URL"),
                os.getenv("SUPABASE_ANON_KEY"),
            )

        return cls._client