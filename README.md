![sample1](https://github.com/MikMakQT/Lunchbot/assets/122342899/84da1718-d25f-43d2-810c-4c5199cb9ede)
# Lunchbot

This Python project focuses on scraping restaurant menus in the Lappeenranta area and sharing them on a designated Slack channel. Users can vote and voting results will be updated automatically.

## Key Features
1. **Web Scraping:** The project utilizes web scraping to extract relevant information from restaurant menus' HTML pages.
2. **Data Parsing:** Once the HTML is scraped, the data is parsed to extract the lunch menus.
3. **Slack Integration:** The processed data is sent to a specified Slack channel using the Slack API and uses to SocketModeHandler for handling voting interaction.
4. **Interactive Voting:** Recipients on the Slack channel can use buttons to easily vote for the restaurant of their choice.
5. **Voting Updates:** The voting results are automatically updated in real-time, providing instant results for the user.

## Install
Tested Python versions: 3.10.11, 3.12.1, 3.11.7

Before running the project, ensure you have python installed and prerequisites installed:

Python Download:
https://www.python.org/downloads/

### Requirements (requirements.txt)

The Requirements file contains all the necessary libraries that the code needs to run.

Dependencies are installed using requirements.txt:

pip install -r requirements.txt

## Creating and Installing an App to your own Slack Workspace Oskari
1. From the Slack menu, select "Add apps" => "App directory".
2. Choose "build" => "your apps".
3. Select "Create new app" => "From scratch".
4. Enter the app's name.
5. Choose the workspace where you want to create the app => "Create app".
6. Navigate to "Basic information" in the menu => "Install your app" => "Permission scope".
7. Add the following permissions:
- chat:write.customize
- chat:write => "Add an OAuth Scope" => "Install to workspace" => "Allow".
8. Go back to the Slack homepage => right-click on the app you created => "Add this app to channel".
9. Select the channel where you want to add the app => "Add".

## App settings

### Tokens (.env)

After creating App you should to go to your App settings and find Basic Information tab using the left menu:

Look for => App-Level Tokens.\
Press => Token and Scopes and give a name for the app.\
Press => Add Scope and give permission connections:write and press Generate.\
Press your App => Copy App level token, which should start like this: xapp-\
Go to your .env file => Paste your token.

Then go to OAuth & Permissions tab using the left menu:

Look for => OAuth Tokens for Your Workspace.\
Copy your => Bot User OAuth Token.\
Go to your .env file => Paste your token.

Inside your .env file should look like this:

SLACK_APP_TOKEN = xapp-*************

SLACK_TOKEN = xoxb-**********

### Socket Mode
Turning on Socket Mode will route your app’s interactions and events over a WebSockets connection instead sending these payloads to Request URLs, which are public HTTP endpoints.

Go to Socket Mode tab using the left menu:
Press => Enable Socket Mode

## Scraping (ruokapaikat.py)

### Principle
The script uses the URL of the website as shown in the first example below to scrape the website. Then the script searches the classes and elements using given parameters.
The parameters given differ page to page. Therefore parameters that work for "lounaat.info" might not work for another page. 

### Changing the URL
Put websites URL you wanna scrape the information inside the ''\
example. html_text = requests.get('https://www.lounaat.info/lounas/pancho-villa/lappeenranta').text

### Removing the Restaurant
To successfully remove a restaurant from the script you need to remove:

( "#" corresponds to the restaurant number in ruokapaikat.py)

FROM MAIN.PY:

Restaurant name from "all_restaurants"

menu# = find_ruoka#

for loop which corresponds to the restaurant (i.e. ruokana in menu1)

res# = [all_restaurants[#]]
res# = ''.join(res#)

FROM RUOKAPAIKAT.PY:

def find_ruoka#():

### Changing the parameters for the searched elements
Websites are constructed different ways, using different class names and elements.\
You can modify searched elements in method find_all()\
example. datas = soup.find_all('div', class_="item")

### How to add more restaurants (Scaling)
Täytä (Mikael M)

## Time (aika.py) Jussi

Täytä

## Running code locally Jussi

Täytä

## Errors
### requirements.txt install error

error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for multidict
Failed to build multidict
ERROR: Could not build wheels for multidict, which is required to install pyproject.toml-based projects

To fix this you can use pip install --upgrade setuptools in terminal

If that doesnt work you need to install C++ Build tools downloading it from Microsoft website https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022

You can also use Visual Studio installer and select C++ package to install and it will fix the error too.


## Avatar
![T0615Q9B316-U0603QHDF7Z-2acdd59bc471-512](https://github.com/MikMakQT/Lunchbot/assets/122342899/61bc8002-009c-495f-afe2-9ce4f77ad993)
