# DBのセットアップ用スクリプト
import os
import psycopg2

class psql_save(object):
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.environ['RDS_HOST'],
            database=os.environ['RDS_DATABASE'],
            user=os.environ['RDS_USERNAME'],
            password=os.environ['RDS_PASSWORD'],
            port="5432")
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def insert_user_info(self, slave_screen_name, user):
        self.cursor.execute(
            '''INSERT INTO for_research.user_info VALUES (%s, %s, %s, %s, %s, %s, %s)''',
            (
                slave_screen_name,
                user['id'],
                user['screen_name'],
                user['friends_count'],
                user['followers_count'],
                user['description'],
                int(user['protected'])
            )
        )

    def insert_status(self, user_id, screen_name, status_id, text):
        self.cursor.execute(
            '''INSERT INTO for_research.status_info VALUES (%s, %s, %s, %s)''',
            (user_id, screen_name, status_id, text))

    def insert_friends(self, user_id=None, screen_name=None, friend_ids=None, value_list=None):
        if value_list != None:
            self.cursor.execute(
                '''INSERT INTO for_research.friend_ids VALUES (%s, %s, %s) ''' + value_list
            )
        else:
            self.cursor.execute(
                '''INSERT INTO for_research.friend_ids VALUES (%s, %s, %s)''',
                (user_id, screen_name, friend_ids)
            )


    def close_section(self):
        self.cursor.close()
        self.conn.close()
