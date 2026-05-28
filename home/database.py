
import psycopg2


def connect_to_database():
    try:
        conn = psycopg2.connect(
            host="localhost",   # use 127.0.0.1 on Windows
            port=5432,          # Postgres default port
            user="vishnu",
            password="bichu@#123",
            dbname="vishnu"     # make sure this database exists
        )
        print("Database connection successful")
        return conn
    except Exception as e:
        print("Database connection failed:", e)


def create_database():
    conn = connect_to_database()
    cur = conn.cursor()
    try:
        # Check table existence using information_schema
        cur.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'enquire'
            );
        """)
        exists = cur.fetchone()[0]


        if not exists:
            cur.execute("""
                CREATE TABLE enquire (
                    id SERIAL PRIMARY KEY,
                    email VARCHAR(255) UNIQUE,
                    description TEXT
                )
            """)
            conn.commit()
        else:
            print("Table 'enquire' already exists")

    except Exception as e:
        print("Error creating table:", e)
       
    finally:
        cur.close()
        conn.close()



