import sys
import os

# Add parent directory to path for imports
current_dir = os.path.dirname(os.path.realpath(__file__))
app_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(app_dir)

import psycopg2
import pandas as pd
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

        try:
            conn = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port,
            )
        except (Exception, psycopg2.DatabaseError) as error:
            self.logger.error(error)
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

    def tabls(self):
        """Get all table names"""
        self.cursor.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        )
        return [table[0] for table in self.cursor.fetchall()]

    def columns(self, table_name: str, with_uuid: bool = False):
        """Get all columns from a table"""
        self.cursor.execute(
            f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'"
        )
        columns = [column[0] for column in self.cursor.fetchall()]
        if not with_uuid:
            columns.remove("uuid")
        return columns

    def row_exists(self, table_name: str, row: pd.Series) -> bool:
        """Check if a row exists in a table"""
        columns = list(row.index)
        values = list(row.values)
        clause = " AND ".join(
            [f"{column} = '{value}'" for column, value in zip(columns, values)]
        )
        sql = f"SELECT * FROM {table_name} WHERE {clause}"
        self.cursor.execute(sql)
        return self.cursor.fetchone() is not None

    def insert(self, table_name: str, dataframe: pd.DataFrame):
        def format_values(row: pd.Series) -> tuple:
            """Format values for SQL query"""
            return tuple(row.values)

        columns = list(dataframe.columns)
        # insert each row of the dataframe into the table
        for i, row in dataframe.iterrows():
            # check if row already exists
            if self.row_exists(table_name, row):
                continue

            values = format_values(row)
            placeholders = ", ".join(["%s"] * len(columns))
            columns_str = ", ".join(columns)
            sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})"
            self.cursor.execute(sql, values)

        self.conn.commit()
        self.logger.info(f"Inserted {len(dataframe)} rows into {table_name}")

    def get(self, table_name: str, where: dict = None) -> pd.DataFrame:
        """Get rows from a table"""
        if where is None:
            sql = f"SELECT * FROM {table_name}"
        else:
            clause = " AND ".join([f"{k} = '{v}'" for k, v in where.items()])
            sql = f"SELECT * FROM {table_name} WHERE {clause}"

        columns = self.columns(table_name, with_uuid=True)
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        df = pd.DataFrame(rows, columns=columns)

        self.logger.info(f"get returned {len(df)} rows from {table_name}")
        return df

    def __str__(self) -> str:
        return f"Database: {self.db_name} at {self.db_host}:{self.db_port}"


if __name__ == "__main__":
    db = Database()
    db.connect()
    db.close()
