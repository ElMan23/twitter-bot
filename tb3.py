import os
import tweepy

# Get tokens from ENV
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET'] 

# Authenticate to Twitter
auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='linux').items(5):
    print()
    print("=-=-=-=-=-=-=-=-=-=-=-=-")   
    print("Here's a new tweet:")
    print("------------------------")   
    print(tweet.text)
    print("LENGTH: " + str(len(tweet.text))) 
    print()