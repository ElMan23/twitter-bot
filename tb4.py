################################################################
# 
# Prints some tweets
# 
################################################################

import os
import tweepy

# Get tokens from ENV
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET'] 
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# for status in tweepy.Cursor(api.user_timeline).items():
#     # process status here
#     process_status(status)

# Only iterate through the first 200 statuses
for status in tweepy.Cursor(api.user_timeline).items(5):
    print(status.text)

# # Only iterate through the first 3 pages
# for page in tweepy.Cursor(api.user_timeline).pages(3):
#     process_page(page)