# DBのセットアップ用スクリプト
import psycopg2

class psql_save(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="twitter_analytics",
            port="5432",
            user="rui",
            password="password"
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()



    def recreate_tables(self):
        self.cursor.execute('CREATE SCHEMA twitter')
        self.cursor.execute('DROP TABLE IF EXISTS twitter.user_info')
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS twitter.user_info (
                    user_id BIGINT,
                    screen_name TEXT,
                    friends_count INT,
                    followers_count INT,
                    self_discription TEXT,
                    PRIMARY KEY(user_id)
                )
            ''')

        self.cursor.execute('DROP TABLE IF EXISTS twitter.status_info')
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS twitter.status_info (
                    user_id BIGINT,
                    screen_name TEXT,
                    status_id BIGINT,
                    status_text TEXT,
                    PRIMARY KEY(status_id)
                )
            ''')


    def insert_user_info(self, user):
        self.cursor.execute(
            '''INSERT INTO twitter.user_info VALUES (%s, %s, %s, %s, %s)''',
            (
                user['id'],
                user['screen_name'],
                user['friends_count'],
                user['followers_count'],
                user['description']
            )
        )

    def insert_status(self, user_id, screen_name, status_id, text):
        self.cursor.execute(
            '''INSERT INTO twitter.status_info VALUES (%s, %s, %s, %s)''',
            (
                user_id,
                screen_name,
                status_id,
                text
            )
        )

    def close_section(self):
        self.cursor.close()
        self.conn.close()
