import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

class DatabaseConnector:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=os.getenv("HOST"),
                port=os.getenv("PORT"),
                database=os.getenv("DATABASE"),
                user=os.getenv("USERDB"),
                password=os.getenv("PASSWORD")
            )
            print("\nConnected to the database!")
        except (psycopg2.Error) as e:
            print(f"\nError connecting to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("\nDisconnected from the database!")

    def execute_query(self, query, values=None, type = "get"):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            self.connection.commit()
            print("\n Query executed successfully!")
            if type == "insert":
                return
            else:
                return cursor.fetchall()
        except (psycopg2.Error) as e:
            print(f"\nError executing query: {e}")
            return None
