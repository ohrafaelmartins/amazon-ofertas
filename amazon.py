import os
import logging
import tweepy

# Configure the logging module
logging.basicConfig(level=logging.ERROR)  # Set the logging level to ERROR

# Create a logger instance
logger = logging.getLogger(__name__)


def authenticate():
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
    BEARER_TOKEN = os.environ['BEARER_TOKEN']
    
    return tweepy.Client(
        bearer_token=BEARER_TOKEN,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET
    )

def tweet_text():
    tt = []
    tt.append("Teste")
    tt.append("Segundo Teste")
    tt.append("Terceiro Teste com hastag")
    return tt

if __name__ == "__main__":
    api = authenticate
    api.create_tweet(text='\n'.join(tweet_text))
    