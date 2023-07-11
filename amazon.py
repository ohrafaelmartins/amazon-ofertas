import os
import logging
import tweepy

# Twitter API credentials
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
BEARER_TOKEN = os.environ['BEARER_TOKEN']


# Authenticate to Twitter
api = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET
)

# Create a tweet
tt = []
tt.append("Teste")
tt.append("Segundo Teste")
tt.append("Terceiro Teste com hastag")

# Post the tweet
api.create_tweet(text='\n'.join(tt))
