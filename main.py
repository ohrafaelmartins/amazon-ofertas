from cgi import test
import requests
import json
# import pandas as pd
import time
import os
from datetime import datetime
import csv
import tweepy


def imprimir():
    data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')

    json_data = json.loads(data.content)

    candidato = []
    # partido = []
    votos = []
    porcentagem = []

    tt = []

    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")

    tt.append(f"Horário: {currentTime}")
    tt.append(f"Urnas apuradas: {json_data['pst']}%")

    for informacoes in json_data['cand']:

        if informacoes['seq'] in ['1', '2', '3', '4']:

            candidato.append(informacoes['nm'])

            c = informacoes['nm'].replace("JAIR BOLSONARO", "Geno&Cida")
            v = informacoes['vap']
            p = informacoes['pvap'] + ' %'
            tt.append("")
            tt.append(f"{c} - Votos:{v} - {p}")

            fields = [currentTime, c, v, p]

            with open(r'resultado-hora-a-hora.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)

    print(*tt, sep='\n')

    time.sleep(10)
    os.system('clear')
    os.system('cat resultado-hora-a-hora.csv')
    print('\n')
    # imprimir()


imprimir()
