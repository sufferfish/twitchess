from twitter import *
import sqlite3
from secrets import * 


# Handles Twitter authentication and API setup.
t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Retreiving Twitter mentions with chess moves
#chessMoves = t.

# Hard coding for now; later can take as input or whatever is necessary
USER_ID = "Chessbot4" 

# Wrapping Twitter GETs in a try/catch in case we encounter an error/exception
try:
    tweets = t.statuses.user_timeline(screen_name=USER_ID)
    for t in tweets:
        print(t['text'])

# Catching an exception; look up API docu on more specific exceptions if we want to addr them case-by-case
except Exception as e:
    print('Exception')
    print(e)
