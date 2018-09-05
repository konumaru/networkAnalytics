import os
import pickle
import random
from tqdm import tqdm

from functions import twitter


def main():
    tw = twitter()
    # 対象スクリーンネームの指定
    screen_name = 'rui_308'
    # フォロワーのidを取得
    filepath = './data/follower_ids.pickle'
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            follower_ids = pickle.load(f)
    else:
        follower_ids = tw.getFollowerIds(screen_name=screen_name)
        with open(filepath, 'wb') as f:
            pickle.dump(follower_ids, f)
    # idリストからユーザー情報の取得
    tw.getUserInfo(query_screen_name=screen_name, ids=follower_ids)


if __name__=='__main__':
    main()