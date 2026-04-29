import psycopg2
import pandas as pd

class PostgresConnectorContextManager:
    def __init__(self, db_host: str, db_name: str, user: str = None, password: str = None, port: int = 5432):
        self.db_host = db_host
        self.db_name = db_name
        self.user = user
        self.password = password
        self.port = port
        self.conn = None

    def __enter__(self):
        self.conn = psycopg2.connect(
            host=self.db_host,
            database=self.db_name,
            user=self.user,
            password=self.password,
            port=self.port
        )
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.conn:
            self.conn.close()

    def get_data_sql(self, sql):
        return pd.read_sql(sql, self.conn)