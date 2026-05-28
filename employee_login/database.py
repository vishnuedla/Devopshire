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
        print("Database connection failed:")





def verify_employee(username, password):
    conn = connect_to_database()
    if conn is None:
        return False

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM employee WHERE username = %s AND password = %s",
        (username, password)
    )
    employee = cur.fetchone()
    cur.close()
    conn.close()
    return employee is not None
