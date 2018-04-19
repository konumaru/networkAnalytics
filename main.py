import json
from requests_oauthlib import OAuth1Session

CK = 'LElwHZGEzo53rW9GAX4QMfR3Y'                             # Consumer Key
CS = '23kDKezl93HC6vDZfFF3FxzwNoFEDzKnDWyoPDGknHIi38R2Bu'         # Consumer Secret
AT = '980825342217629696-XX36Z2GHh61sHfQ5x3QoGST0ht8fTyj' # Access Token
AS = 'rlwIVxOJpDXNBpwSmvfhOrvZYK4bPYQFo6vs5jgBICW7k'         # Accesss Token Secert

# ツイート投稿用のURL
# url = "https://api.twitter.com/1.1/statuses/update.json"
url = 'https://api.twitter.com/1.1/friends/list.json'

# ツイート本文
# params = {"status": "Hello, World!"}
params = {'screen_name': 'rk_biscuit'}

# OAuth認証で POST method で投稿
api = OAuth1Session(CK, CS, AT, AS)
# req = api.post(url, params = params)
#
# # レスポンスを確認
# if req.status_code == 200:
#     print ("OK")
# else:
#     print ("Error: %d" % req.status_code)

def make_params():
    query = '猫 filter:images min_replies:10 min_retweets:500 min_faves:500 exclude:retweets'
    params = {
        'q': query,
        'count': 20
    }

    return params

def search_tweet(api, params):
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    req = api.get(url, params=params)

    result = []
    if req.status_code == 200:
        tweets = json.loads(req.text)
        result = tweets['statuses']
    else:
        print("ERROR!: %d" % req.status_code)
        result = None

    assert(len(result) > 0)

    return result

params = make_params()
print (search_tweet(api, params)[0])
