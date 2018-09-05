import os
import json
import time
import random
import numpy as np
from db import psql_save
from requests_oauthlib import OAuth1Session


class twitter():
    def __init__(self):
        CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
        ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
        ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']
        self.api = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

    # 特定ユーザーフォロワーidリストを取得
    def getFollowerIds(self, screen_name):
        ids = []
        cursor = -1
        url = 'https://api.twitter.com/1.1/followers/ids.json?'
        params = {'screen_name': screen_name}

        while cursor != 0 and len(ids)<50000:
            req = self.api.get(url, params=params)
            if req.status_code == 200:
                temp = json.loads(req.text)
                ids.extend(temp['ids'])
                cursor = temp['next_cursor']
                params['cursor'] = temp['next_cursor']
                time.sleep(10*random.uniform(0.5,1.5))
                print('totalGetFollowerNum: {0}'.format(len(ids)))
            else:
                print ("Error: %d at getFollowerIds" % req.status_code)

        return ids


    # 特定ユーザーフォローidリストを取得
    def getFriendIds(self, screen_name):
        ids = []
        cursor = -1
        url = 'https://api.twitter.com/1.1/friends/ids.json'
        params = {'screen_name': screen_name}

        while cursor != 0:
            req = self.api.get(url, params=params)
            if req.status_code == 200:
                temp = json.loads(req.text)
                ids.extend(temp['ids'])
                cursor = temp['next_cursor']
                params['cursor'] = temp['next_cursor']
                time.sleep(10*random.uniform(0.5,1.5))
                # print('totalGetFriendNum: {0}'.format(len(ids)))
            elif req.status_code == 429:
                print('Too Many Requests')
                time.sleep(20*60*random.uniform(0.5,1.5))
            elif req.status_code == 401:
                print('This user is Unauthorized')
                return list()
            elif req.status_code == 404:
                print ('This user is Not Found')
            else:
                print ("Error: %d at getFriendIds" % req.status_code)

        return ids


    # user_idからユーザー情報の取得
    def getUserInfo(self, query_screen_name, ids):
        url = 'https://api.twitter.com/1.1/users/lookup.json'
        ids = np.array(ids).astype(str)
        psql = psql_save()

        for i in range(0, len(ids), 100):
            _ids = ','.join(ids[i:i+100])
            params = {'user_id': _ids}

            req = self.api.get(url, params=params)
            if req.status_code == 200:
                req_text = json.loads(req.text)
                for user in req_text:
                    try:
                        psql.insert_user_info(query_screen_name, user)
                    except:
                        print ("Error: %d at getUserInfo()" % req.status_code)

            time.sleep(2*random.uniform(0.5,1.5))


    def getUserStatuses(self, screen_name):
        url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        params = {'screen_name': screen_name, 'count': 100}
        psql = psql_save()

        req = self.api.get(url, params=params)
        if req.status_code == 200:
            req_text = json.loads(req.text)
            for status in req_text:
                try:
                    psql.insert_status(status['user']['id'], status['user']['screen_name'], status['id'], status['text'])
                except:
                    pass
        else:
            print ("Error: %d at getUserInfo()" % req.status_code)
