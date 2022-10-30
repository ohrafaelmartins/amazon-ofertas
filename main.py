from cgi import test
import secrets
import requests
import json
# import pandas as pd
import time
import os
from datetime import datetime
import csv
import tweepy

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


def imprimir():
    data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')

    json_data = json.loads(data.content)

    tt = []

    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")

    tt.append("Resultados das eleições presidenciais")
    tt.append(f"Horário: {currentTime}")
    tt.append(f"Urnas apuradas: {json_data['pst']}%")

    for tse in json_data['cand']:

        if tse['seq'] in ['1', '2', '3', '4']:

            c = tse['nm'].replace("JAIR BOLSONARO", "inominável")
            v = tse['vap']
            p = tse['pvap'] + ' %'
            tt.append("")
            tt.append(f"{c} - votos:{v} - {p}")

            fields = [currentTime, c, v, p]

            with open(r'resultado-hora-a-hora.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)

    tt.append("#LulaPresidente2022, #Eleicao2022")
    # api.create_tweet(text='\n'.join(tt))

    time.sleep(1)
    os.system('clear')
    os.system('cat resultado-hora-a-hora.csv')

imprimir()
