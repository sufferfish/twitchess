from twitter import *
from secrets import * 
import requests
import json
import base64
import tweepy

# Handles Twitter authentication and API setup.
t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Hard coding for now; later can take as input or whatever is necessary
USER_HANDLE = "Chessbot4" 
USER_ID = 1354261508859957249

# Generates URL to get mentions
def create_url_get_tweets_with_mentions():
    return 'https://api.twitter.com/2/users/{}/mentions'.format(USER_ID)

# Generate headers for cURL requests
# Metadata send with the cURL request
def create_headers():
    headers = {
            "Authorization": 
               "Bearer {}".format(bearer_token),
            }
    return headers

def parameters():
    # https://developer.twitter.com/en/docs/twitter-api/tweets/timelines/api-reference/get-users-id-mentions
    # Query Parameters
    return {"tweet.fields": "author_id"} 

# Make the GET request
def connect_to_endpoint(url):
    headers = create_headers()
    parameter = parameters()
    response = requests.request("GET", url, headers=headers, params=parameter)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    return response.json()

def auth_user():
    key_secret = '{}:{}'.format(consumer_key, consumer_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    auth_url = 'https://api.twitter.com/oauth2/token'
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
            'grant_type': 'client_credentials'
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json()['access_token']
    return access_token

def auth_user_tweepy():
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(token,token_secret)
    api=tweepy.API(auth)
    return api

def post_tweet(data):
    '''post_headers = {
            'Authorization': 'Bearer {}'.format(auth_user)
    }
    post_tweet_url = 'https://api.twitter.com/1.1/statuses/update.json'
    post_params = {
            'status': data
    }
    
    response = requests.post(post_tweet_url, headers=post_headers, params=post_params)
    print(response.status_code)
    print(response.json())'''
    api = auth_user_tweepy()
    api.update_status(data)

# Wrapping Twitter GETs in a try/catch in case we encounter an error/exception
try:
    #tweets = t.statuses.user_timeline(screen_name=USER_HANDLE)
    #for t in tweets:
    #    print(t['text'])
    url = create_url_get_tweets_with_mentions()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    for tweet in json_response['data']:
        print(tweet['author_id'])

    post_tweet("posting test")
# Catching an exception; look up API docu on more specific exceptions if we want to addr them case-by-case
except Exception as e:
    print('Exception')
    print(e)
