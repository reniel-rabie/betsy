import psycopg2
import os
from config import setup_logger
from dotenv import load_dotenv

load_dotenv()


class Database:
    def __init__(self) -> None:
        self.logger = setup_logger(self.__class__.__name__)
        self.db_name = os.getenv("POSTGRES_DB")
        self.db_user = os.getenv("POSTGRES_USER")
        self.db_password = os.getenv("POSTGRES_PASSWORD")
        self.db_host = "127.0.0.1"
        self.db_port = "5432"

        self.conn = None
        self.cursor = None

    def connect(self):
        """Connect to the PostgreSQL database server"""
        self.logger.info("Connecting to the PostgreSQL database...")

        print(f"DB: {self.db_name}")
        print(f"USER: {self.db_user}")
        print(f"PASSWORD: {self.db_password}")

        conn = psycopg2.connect(
            database=self.db_name,
            user=self.db_user,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
        )
        self.logger.info("Database opened successfully")
        self.conn = conn
        self.cursor = conn.cursor()


if __name__ == "__main__":
    db = Database()
    db.connect()
