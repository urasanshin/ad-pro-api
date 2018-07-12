from chalice import Chalice
import requests
from time import sleep
import os
import json  # 標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session  # OAuthのライブラリの読み込み
app = Chalice(app_name='urakamipa')


@app.route('/', content_types=['application/json'
                               ],
           cors=True)
def index():



    wait_time = 0.3  # (sec)
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?language=ja&address={}&key=AIzaSyD2n8ALJPQW6y08OsVxU7JhZfQZTP8P3V8'
    headers = {'content-type': 'application/json'}


    CK = os.environ["CONSUMER_KEY"]
    CS = os.environ["CONSUMER_SECRET"]
    AT = os.environ["ACCESS_TOKEN"]
    ATS = os.environ["ACCESS_TOKEN_SECRET"]
    twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"  # タイムライン取得エンドポイント

    params = {'count': 6}  # 取得数
    res = twitter.get(url, params=params)
    queries = []
    if res.status_code == 200:  # 正常通信出来た場合
        timelines = json.loads(res.text)  # レスポンスからタイムラインリストを取得
        for line in timelines:  # タイムラインリストをループ処理
            # print(line['text'])#タイムラインのみ
            queries.append(line['text'])
        # print(line['user']['name']+':'+line['text'])#ユーザー名とタイムライン
        # print(line['created_at'])#ツイートした日時
        # print('*******************************************')
    else:  # 正常通信出来なかった場合
        print("Failed: %d" % res.status_code)

    # queries = []
    # with open('./queries', 'r') as f:
    #     queries = f.readlines()

    # import getTimelines
    # with open('./', 'r') as f:
    # gTa = f.readlines()

    results = []
    for q in queries:
        q = q.strip()
        url = base_url.format(q)
        r = requests.get(url, headers=headers)
        data = r.json()
        if 'results' in data and len(data['results']) > 0 and 'formatted_address' in data['results'][0]:
            results.append( {
                #'formatted_address':data['results'][0]['formatted_address'],
                'lat':data['results'][0]['geometry']['location']['lat'],
                'lon':data['results'][0]['geometry']['location']['lng']
            }
            )
            # results.append('{}@{}@{}@{}'.format(
            #     q,
            #     data['results'][0]['formatted_address'],
            #     data['results'][0]['geometry']['location']['lat'],
            #     data['results'][0]['geometry']['location']['lng']
            # ))
        else:
            results.append('{}@ @ @ '.format(q))
        sleep(wait_time)

    return {'results':results}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
