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
Tested Python versions: 3.10.11, 3.11.1, 3.11.7, 3.12.1 (should work with all 3.0+ python versions)

Before running the project, ensure you have python installed and requirements installed:

Python Download:
https://www.python.org/downloads/

### Requirements (requirements.txt)

The Requirements file contains all the necessary libraries that the code needs to run.

Dependencies are installed using requirements.txt:

pip install -r requirements.txt

## Creating and Installing an App to your own Slack Workspace
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

To successfully add a restaurant to the script you need to add:

( "#" corresponds to the restaurant number in ruokapaikat.py)

TO MAIN.PY:

voter_ids#

vote_count#

for loop which corresponds to the restaurant (i.e. ruokana in menu1)

global vote_count#

vote_count = len(voter_ids#)

res# = [all_restaurants[#]]
res# = ''.join(res#)

TO RUOKAPAIKAT.PY:

(note: All websites are built differently so the code you use must reflect this)

def find_ruoka#():

## Time (aika.py) Jussi

Defines a function called "aika" (Finnish for "time") that returns the current date as a string in the format "day.month". 
It uses the date.today() method from the datetime module to get the current date, then extracts the day and month components. 
These are then formatted as a string and returned. 
The time functions ultimately provide the daily lunch menus of restaurants to the team's Slack channel at 10 am automatically, either locally or in the cloud.

## Running code automatically and locally with Task Scheduler Jussi

To run these functions locally, you would need to have Python and the BeautifulSoup library installed on your computer. 
You would then copy and paste the code into a Python script and run the script in a Python environment. 
The functions will execute and print out the menu items for each restaurant as a list of Python objects.
1. Clone the repository to your local machine using Git. Navigate to the directory where you want the project to be stored and run. Remember to install dependencies!
2. Set up a Virtual Environment (optional but recommended). 
You can create a virtual environment using venv. Open a terminal within VSCode (Terminal > New Terminal) and navigate to your project directory.
3. Monitor the output: As your script runs, you should see output in the terminal indicating the progress of your scraping, voting, or any other operations your script performs.

    AND
1. More of python script, run scheduled Python scripts
2. Adding a new "trigger" which you can design to add time task to run LounasBot every day 10am when there is food available. After that you can change duration of script and repeating time.
3. Remember to "Enable" trigger!!
4. Add new action which is starting the program and adding the path to program on Windows command prompt
5. If you want more information running the code with Task scheduler under is video about the task scheduler
  
https://www.youtube.com/watch?v=4n2fC97MNac&t=249s


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


## LunchBot Avatar (created using AI)
![T0615Q9B316-U0603QHDF7Z-2acdd59bc471-512](https://github.com/MikMakQT/Lunchbot/assets/122342899/61bc8002-009c-495f-afe2-9ce4f77ad993)
