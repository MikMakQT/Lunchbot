# Lunchbot
LounasBotti

This projects goal is to web scrape restaurants menus in the Lappeenranta area.\
After scraping HTML, desired data is searched and parsed.\
Processed data is then send to desired Slack channel using Slack API.\
Recipients can vote interactively which restaurant to go using buttons

## Install
Python Download:\
https://www.python.org/downloads/

Dependencies are installed using requirements.txt:\
pip install -r requirements.txt

## File modifications (.env)
Go to https://api.slack.com/apps and create App.\
After you created App, you should be in the App settings, go to OAuth & Permissions using the left menu:

Look for => OAuth Tokens for Your Workspace.\
Copy your => Bot User OAuth Token.

Inside code editor head over .env file\
Paste your OAuth Token\
example. SLACK_TOKEN = xoxb-**********

## Scraping (ruokapaikat.py)

### Principle
The script uses the URL of the website as shown in the first example below to scrape the website. Then the script searches the classes and elements using given parameters.
The parameters given differ page to page. Therefore parameters that work for "lounaat.info" might not work for another page. 

### Removing or Changing the URL
Put websites URL you wanna scrape the information inside the ''\
example. html_text = requests.get('https://www.lounaat.info/lounas/pancho-villa/lappeenranta').text

### Changing the parameters for the searched elements
Websites are constructed different ways, using different class names and elements.\
You can modify searched elements in method find_all()\
example. datas = soup.find_all('div', class_="item")

## Time (aika.py)

### Principle

## Requirements (requirements.txt)

### Principle

## Errors
#1 C++ Error
If you get error like this when installing packages: 
error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for multidict
Failed to build multidict
ERROR: Could not build wheels for multidict, which is required to install pyproject.toml-based projects
To fix this you can use pip install --upgrade setuptools in terminal
If that doesnt work you need to install C++ downloading it from Microsoft website https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022
or using Visual Studio installer and select C++ package to install
