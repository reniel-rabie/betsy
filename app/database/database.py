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
        self.connect()

    def connect(self):
        """Connect to the PostgreSQL database server"""
        self.logger.info("Connecting to the PostgreSQL database...")

        try:
            conn = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port,
            )
        except ConnectionError as e:
            self.logger.error(e)
            return False
        
        self.conn = conn
        self.cursor = conn.cursor()
        self.logger.info("Database connected succesfully")
        return True

        

    def close(self):
        """Close the connection to the PostgreSQL database server"""
        self.conn.close()
        self.logger.info("Database closed successfully")

    def init_database(self):
        """Initialixe the database from the init.sql file"""
        init_file = "database/init.sql"
        self.logger.info("Initializing the database...")
        with open(init_file, "r") as f:
            sql = f.read()
            self.cursor.execute(sql)
            self.conn.commit()
        self.logger.info("Database initialized successfully")

    def table_names(self):
        """Get all table names"""
        self.cursor.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        )
        return [table[0] for table in self.cursor.fetchall()]

    def columns(self, table_name: str):
        """Get all columns from a table"""
        self.cursor.execute(
            f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'"
        )
        return [column[0] for column in self.cursor.fetchall()]


if __name__ == "__main__":
    db = Database()
    db.connect()
    db.close()
