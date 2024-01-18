import slack
from slack_sdk import WebClient
from bs4 import BeautifulSoup 

import os
from pathlib import Path
from dotenv import load_dotenv

from fpdf import FPDF
import requests
import time
from datetime import date

env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


client = WebClient(token=os.environ['SLACK_TOKEN'])





def find_ruoka():
    #RUOKALISTA SIVUN KOKO HTML TEKSTI
    html_text = requests.get('https://wolkoff.fi/ruoka-juoma/').text
    #SIVULLE TEHTIIN JOTAIN XD
    soup = BeautifulSoup(html_text,'lxml')
    #LÖYDETÄÄN KAIKKI LI, MENU-LIST_ITEM, koska sieltä löytyy ruokalistan sisältö
    datas = soup.find_all('li', class_="menu-list__item")

    #PÄIVÄMÄÄRÄ TÄNÄÄN
    today = date.today()

    datetime_month = today.month
    datetime_day = today.day
    #YHDISTETÄÄN PÄIVÄ JA KUUKAUSI
    aika_tänään = (f'{datetime_day}.{datetime_month}')
    #MUUTETAAN STRING MUOTOON
    inputText = aika_tänään
    
    for data in datas:
        data = data.text
        #JOS TÄMÄ PÄIVÄMÄÄRÄ LÖYTYY RUOKALISTALTA, ruokalista tulostuu slackkiin
        if inputText in data:
            print(data, end='')
            kaava = data
            client.chat_postMessage(channel='#lunch-bot', text = (f'Tänään ruokana:\n {kaava}'))
            break
        else:
            #VIIKONLOPPU TAI EI RUOKAILUA
            print("ei ruokailua")
        






find_ruoka()
