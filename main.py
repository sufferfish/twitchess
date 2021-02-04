import tweepy
from secrets import * 
import requests
import json
import base64

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

def auth_user_tweepy():
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(token,token_secret)
    api=tweepy.API(auth)
    return api

def post_tweet(data):
    api = auth_user_tweepy()
    api.update_status(data)

def get_mentions():
    api = auth_user_tweepy()
    mentions = api.mentions_timeline(count = 5)
    screenNamesList = []
    textList = []
    for mention in mentions:
        #print(mention.text[11:]) #strips '@Chessbot4' from mentions for cleaner data
        #print(mention.user.screen_name)
        screenNamesList.append(mention.user.screen_name)
        textList.append(mention.text[10:])

    mentionData = dict(zip(screenNamesList, textList))
    print(mentionData)
    

# Wrapping Twitter GETs in a try/catch in case we encounter an error/exception
try:
    url = create_url_get_tweets_with_mentions()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))
    for tweet in json_response['data']:
        print(tweet['author_id'])

    # post_tweet("posting test")
    get_mentions()
    
# Catching an exception; look up API docu on more specific exceptions if we want to addr them case-by-case
except Exception as e:
    print('Exception')
    print(e)
