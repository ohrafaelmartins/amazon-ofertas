import os
import tweepy

import logging

logging.basicConfig(level=logging.ERROR)
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')


if __name__ == "__main__":
    try:     
        CONSUMER_KEY = os.environ['CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
        ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
        ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
        BEARER_TOKEN = os.environ['BEARER_TOKEN']

        api = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET
        )

        tweet_text = []
        tweet_text.append("Teste")
        tweet_text.append("Segundo Teste")
        tweet_text.append("Terceiro Teste com hastag")

        api.create_tweet(text='\n'.join(tweet_text))
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
