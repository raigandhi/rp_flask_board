import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user="admin",
    password="P4ssw0rd",
    port="5432"
)
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS post;")
cur.execute("""
    CREATE TABLE post (
        id SERIAL PRIMARY KEY,
        created DATE DEFAULT CURRENT_TIMESTAMP,
        author TEXT NOT NULL,
        message TEXT NOT NULL
    );
""")
conn.commit()
cur.close()
conn.close()
