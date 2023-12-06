# Lunchbot\
LounasBotti\

## This project is to web scrape and extract lunch menu information from restaurant websites and process it. /n After processing data is converted to PDF-file, which is then send using Slack API to desired Slack channel. Recipients can vote interactively which restaurant to go using buttons\

## install\
Python Download:\
https://www.python.org/downloads/

Dependencies are installed using requirements.txt:\
pip install -r requirements.txt

## File modifications\
Go to https://api.slack.com/apps and create App.\
After you created App, you should be in the App settings, go to OAuth & Permissions using the left menu.\
Look for => >OAuth Tokens for Your Workspace.
Copy your => >Bot User OAuth Token.

Inside code editor head over .env file\
Copy paste your OAuth Token\
example. SLACK_TOKEN = xoxb-**********

## Changing Scraping URL
Put websites URL you wanna scrape the information inside the ''\
example. html_text = requests.get('https://www.lounaat.info/lounas/cafe-hullu-orava/lappeenranta').text
