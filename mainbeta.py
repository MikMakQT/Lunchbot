from slack_sdk import WebClient
from bs4 import BeautifulSoup 
import slack_sdk
import os
from pathlib import Path
from dotenv import load_dotenv


import requests 

from aika import *
from ruokapaikat import *
from blockkit import Button, Context, Divider, Message, Section

import json

from slack_sdk.webhook import WebhookClient

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


import time

env_path = Path('.') /'.env'
load_dotenv(dotenv_path=env_path)


client = WebClient(token=os.environ['SLACK_TOKEN'])

app = App(token=os.environ["SLACK_TOKEN"])


timestamp1 = ""
user_id = ""
voters = []
voters1 = []
voters2 = []
voters3 = []
size1= []
size2= []
size3= []
res = []
restaurant1 = ['Cafe Hullu','Pancho Villa','Wolkoff']

response = app.client.conversations_list()
channel_name = 'lunch-bot'  # Replace with your channel name
channel_id = None
for channel in response['channels']:
    if channel['name'] == channel_name:
        channel_id = channel['id']
        break
if channel_id:
    print(f"Channel ID for '{channel_name}': {channel_id}")
else:
    print(f"Channel '{channel_name}' not found.")


datas1 = find_ruoka1()
datas2 = find_ruoka2()
datas3= find_ruoka3()
datas4= find_ruoka4()
datas5= find_ruoka5()


    
def ruokanaTänään():

    
    for data in datas1:
        data = data.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in data:
        
            pattern2 = data
            
            pattern2 = data.replace('€', ' euro ')
            res = [restaurant1[0]]
            result = ''.join(res)
            print(pattern2)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'{result}:\n{pattern2}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "button_click1"
                },
                
            }
            ])
            
        
        
        else:
            #Weekend or no meals
            print("ei ruokailua")

    for data in datas2:
        data = data.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in data:
        
            pattern2 = data
            
            pattern2 = data.replace('€', ' euro ')
            res = [restaurant1[1]]
            result = ''.join(res)
            print(pattern2)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'{result}:\n{pattern2}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "button_click2"
                },
                
            }
            ])
            
        
        
        else:
            #Weekend or no meals
            print("ei ruokailua")
    for data in datas3:
        data = data.text
        #If today's date is found on the menu, the menu will be printed to Slack
        if aika() in data:
        
            pattern2 = data
            
            pattern2 = data.replace('€', ' euro ')
            res = [restaurant1[2]]
            result = ''.join(res)
            print(pattern2)
            client.chat_postMessage(channel='#lunch-bot', text="",
            blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f'{result}:\n{pattern2}!'},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Vote"},
                    "action_id": "button_click3"
                },
                
            }
            ])
            
        
        else:
            #Weekend or no meals
            print("ei ruokailua")
    global timestamp1
    answer1=client.chat_postMessage(channel='#lunch-bot', text="Kukaan ei ole äänestänyt vielä")
    timestamp1 = answer1['ts']
    








   
def voting():
    
    global timestamp1
    if timestamp1:
            
            timestamp2 = timestamp1
            res1 = [restaurant1[0]]
            result1 = ''.join(res1)
            res2 = [restaurant1[1]]
            result2 = ''.join(res2)
            res3 = [restaurant1[2]]
            result3 = ''.join(res3)
            if timestamp1:
                global size1
                global size2
                global size3
                #Update the previous message with the current vote count
                client.chat_update(
                channel=channel_id,
                ts=f"{timestamp2}",
                text=f"({size1}) on äänestänyt ravintolaa {result1}, ({size2}) on äänestänyt ravintolaa {result2}, ({size3}) on äänestänyt ravintolaa {result3}"
                )
                
                
            else:
                # Post a new message and store the timestamp
                answer = client.chat_postMessage(
                channel='#lunch-bot',
                text=f"{size1} on äänestänyt ravintolaa {result1}, {size2} on äänestänyt ravintolaa {result2}, {size3} on äänestänyt ravintolaa {result3}",
                timestamp1 = answer['ts'])


@app.action("button_click1")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id not in voters:
        voters.append(user_id)

    # Check if the user has already voted
    if user_id in voters:
        voters1.append(user_id)
        global size1
        voters11 = list(set(voters1))
        size1 = len(voters11)
        voting()
@app.action("button_click2")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id not in voters:
        voters.append(user_id)

    # Check if the user has already voted
    if user_id in voters:
        voters2.append(user_id)
        global size2
        voters22 = list(set(voters2))
        size2 = len(voters22)
        voting()
@app.action("button_click3")
def action_button_click3(body, ack):
    
    ack()
    user_id = body['user']['id']
    if user_id not in voters:
        voters.append(user_id)

    # Check if the user has already voted
    if user_id in voters:
        voters3.append(user_id)
        global size3
        voters33 = list(set(voters3))
        size3 = len(voters33)
        voting()

        
        
     
                

        
   
    
    
    




if __name__ == "__main__":
    ruokanaTänään()
    #client.chat_postMessage(channel='#lunch-bot', blocks=json.dumps(parsed_json))
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
