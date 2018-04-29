import json
import time
import random
from requests_oauthlib import OAuth1Session

def getAPI():
    # キー取得
    with open('key.txt') as f:
        keys = json.load(f)
    # 環境変数から承認情報を取得
    CONSUMER_KEY    = keys['CONSUMER_KEY']
    CONSUMER_SECRET = keys['CONSUMER_SECRET']
    ACCESS_TOKEN    = keys['ACCESS_TOKEN']
    ACCESS_SECRET   = keys['ACCESS_SECRET']
    api = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
    return api


def getFollowerIds(api, screen_name):
    ids = []
    cursor = -1
    url = 'https://api.twitter.com/1.1/followers/ids.json'
    params = {'screen_name': screen_name}

    while cursor != 0:
        params['cursor'] = str(cursor)
        req = api.get(url, params=params)
        temp = json.loads(req.text)

        ids.extend(temp['ids'])
        cursor = temp['next_cursor']
        time.sleep(20*random.uniform(0.5,1.5))
    return ids


def getUserInfoFromIds(api, ids):
    lockup = 'https://api.twitter.com/1.1/users/lookup.json'
    req = api.get(lockup, params={'user_id': id_list})
    req_json = json.loads(req.text)


def main():
    api = getAPI()

    ids = getUserIds(api, screen_name='henjinmajime')

if __name__=='__main__':
    main()
