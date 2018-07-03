# DBのセットアップ用スクリプト
import psycopg2

class psql_save(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="my_db",
            port="5432",
            user="rui",
            password="password"
        )
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()



    def recreate_tables(self):
        self.cursor.execute('DROP SCHEMA IF EXISTS twitter')
        self.cursor.execute('CREATE SCHEMA twitter')
        # ユーザー情報
        self.cursor.execute('DROP TABLE IF EXISTS twitter.follower_user_info')
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS twitter.follower_user_info (
                    slave_screen_name TEXT,
                    user_id BIGINT,
                    screen_name TEXT,
                    friends_count INT,
                    followers_count INT,
                    self_discription TEXT,
                    PRIMARY KEY(user_id)
                )
            ''')
        # ツイート情報
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
        # フォロー情報
        self.cursor.execute('DROP TABLE IF EXISTS twitter.friends')
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS twitter.friends (
                    user_id BIGINT,
                    screen_name TEXT,
                    friend_ids TEXT,
                    PRIMARY KEY(user_id)
                )
            ''')


    def insert_user_info(self, slave_screen_name, user):
        self.cursor.execute(
            '''INSERT INTO twitter.follower_user_info VALUES (%s, %s, %s, %s, %s, %s)''',
            (
                slave_screen_name,
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

    def insert_friends(self, user_id=None, screen_name=None, friends_ids=None, value_list=None):
        if value_list != None:
            self.cursor.execute('''INSERT INTO twitter.friends VALUES '''+value_list)
        else:
            self.cursor.execute(
                '''INSERT INTO twitter.friends VALUES (%s, %s, %s)''',
                (
                    user_id,
                    screen_name,
                    friends_ids
                )
            )


    def close_section(self):
        self.cursor.close()
        self.conn.close()
