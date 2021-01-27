from twitter import *
import sqlite3
from secrets import * 


# Handles Twitter authentication and API setup.
t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Retreiving Twitter mentions with chess moves
chessMoves = t.