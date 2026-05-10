
import psycopg2


def connect_to_database():
    try:
        conn = psycopg2.connect(
            host="postgresql",   # use 127.0.0.1 on Windows
            port=5432,          # Postgres default port
            user="vishnu",
            password="bichu@#123",
            dbname="vishnu"     # make sure this database exists
        )
        print("Database connection successful")
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        


