import json
from requests_oauthlib import OAuth1Session


CK = 'LElwHZGEzo53rW9GAX4QMfR3Y'                             # Consumer Key
CS = '23kDKezl93HC6vDZfFF3FxzwNoFEDzKnDWyoPDGknHIi38R2Bu'         # Consumer Secret
AT = '980825342217629696-XX36Z2GHh61sHfQ5x3QoGST0ht8fTyj' # Access Token
AS = 'rlwIVxOJpDXNBpwSmvfhOrvZYK4bPYQFo6vs5jgBICW7k'         # Accesss Token Secert

# ツイート投稿用のURL
# url = "https://api.twitter.com/1.1/statuses/update.json"
url = 'https://api.twitter.com/1.1/followers/ids.json'
params = {'screen_name': 'rk_biscuit'}


api = OAuth1Session(CK, CS, AT, AS)

req = api.get(url, params=params)
