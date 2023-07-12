import os
import tweepy
import logging
import csv
import sqlite3


logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(format='%(process)d-%(levelname)s-%(message)s')


def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS newer (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    link TEXT,
                    desc TEXT,
                    price TEXT,
                    posted TEXT
                )''')


def insert_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    with open("newer.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            val = line[0].split(',')
            cursor.execute("SELECT * FROM newer WHERE link = ?", (val[0],))
            result = cursor.fetchall()

            print(result)
            if len(result) <= 0:
                query = "INSERT INTO newer (link, desc, price, posted) VALUES (?, ?, ?, ?)"
                cursor.execute(query, val)
                
    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_db()
    insert_db()

    """ try:     
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
        first_line = first_line()
        tweet_text.append(first_line)
        tweet_text.append("Segundo Teste")
        tweet_text.append("Terceiro Teste com hastag")

        #  api.create_tweet(text='\n'.join(tweet_text))
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
 """
