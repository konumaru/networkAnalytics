import psycopg2

conn = psycopg2.connect(
host="localhost",
database="twitter_analytics",
port="5432",
user="kyohei",
password="password"
)
cursor = conn.cursor()
cursor.execute('''
        CREATE TABLE IF NOT EXISTS followers (
        id INT,
        screen_name TEXT,
        num_friends INT,
        num_followers INT,
        self_discription TEXT,
        PRIMARY KEY(id)
        )
    ''')
conn.commit()
