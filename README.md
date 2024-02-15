# Lunchbot
LounasBotti

## Introduction
This Python project focuses on scraping restaurant menus in the Lappeenranta area and sharing them on a designated Slack channel. The goal is to streamline the process of choosing a restaurant among a group of people by allowing them to vote interactively.

## Key Features
1. **Web Scraping:** The project utilizes web scraping techniques to extract relevant information from restaurant menus' HTML pages.
2. **Data Parsing:** Once the HTML is scraped, the data is parsed to extract the desired information, such as menu items, prices, and other relevant details.
3. **Slack Integration:** The processed data is seamlessly sent to a specified Slack channel using the Slack API, ensuring real-time updates for the users.
4. **Interactive Voting:** Recipients on the Slack channel can engage in interactive voting. The project incorporates buttons to facilitate easy voting for the restaurant of their choice.
5. **Live Updates:** The voting results are dynamically updated in real-time, providing instant feedback to users as they cast their votes.

## Install
Tested Python versions: 3.12.1, 
Python Download:\
https://www.python.org/downloads/

Dependencies are installed using requirements.txt:\
pip install -r requirements.txt

## Requirements (requirements.txt)
täytä

## Installing an App to your own Workspace
täytä

## Tokens (.env)
For the App to work in your workspace you need create App and copy your tokens to .env file.
First go to https://api.slack.com/apps and create App.\
After you created App, you should be in the App settings, go to Basic Information tab in the left menu.
Scroll down when you see App-Level Tokens and press Generate Token and Scopes. 
Give the token a name and give scope connections:write.
After that press the token and copy the token. It should look like this: xapp-

Then go to OAuth & Permissions using the left menu:

Look for => OAuth Tokens for Your Workspace.\
Copy your => Bot User OAuth Token.

Inside code editor head over .env file\
Paste your OAuth Token\
example. SLACK_TOKEN = xoxb-**********
Paste your 
example. SLACK_APP_TOKEN = xapp-*********

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
