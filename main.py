from slack_sdk import WebClient
from bs4 import BeautifulSoup 

import os
from pathlib import Path
from dotenv import load_dotenv

import requests

import * from aika
import * from ruokapaikat

env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


client = WebClient(token=os.environ['SLACK_TOKEN'])





def find_ruoka():
       
    for data in datas:
        data = data.text
        #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
        if aika() in data:
            print(data, end='')
            kaava = data
            client.chat_postMessage(channel='#lunch-bot', text = (f'Tänään ruokana:\n {kaava}'))
            break
        else:
            #VIIKONLOPPU TAI EI RUOKAILUA
            print("ei ruokailua")
        






find_ruoka()
