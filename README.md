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

### Requirements (requirements.txt) Oskari
Dependencies are installed using requirements.txt:
pip install -r requirements.txt

selitä mitä tää requirements tekee (ei tarvii olla mikää tosi pitkä joku pari virkettä)

## Creating and Installing an App to your own Slack Workspace Oskari
kirjota step by step ohje miten se app lisätään sinne slackkiin. kannattaa ekaks luoda joku app (ei tää lounaslistabot vaa joku ihan uus) ja sit lisäät sinne slackkiin sen.

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
To remove a restaurant from the message frame you need to remove the following:
From main.py all actions which correspond to the restaurant in ruokapaikat.py.

And finally from ruokapaikat.py remove the find_ruoka# which is now no longer tied to anything in main.py.

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

##Installing to workspace
To install the specified packages into your Visual Studio Code workspace, you'll need to create a requirements.txt file with the listed package names and versions. Here's how you can do it:

Open Visual Studio Code.
Create a new file named requirements.txt in the root directory of your project.
Copy and paste the content into the requirements.txt file

Save the requirements.txt file.
Open the terminal in Visual Studio Code.
Run the following command to install the packages listed in requirements.txt:

pip install -r requirements.txt

This command will install all the packages and their specified versions listed in the requirements.txt file into your Python environment associated with your Visual Studio Code workspace. Make sure you have Python and pip installed and configured correctly.

##Explanation how to install to workspace
The requirements.txt file is a commonly used convention in Python projects to specify the dependencies required by the project. Each line in the file typically represents a separate package that the project depends on, along with the specific version requirements.

Here's a breakdown of each part of the requirements.txt file:

Package Name: This is the name of the Python package required by the project.
Version Specification: This is the version of the package required by the project. It's specified using the syntax ==, followed by the version number.

For example:
aiohttp==3.8.3
This line specifies that the project requires version 3.8.3 of the aiohttp package.

When you have a requirements.txt file in your project, you can use tools like pip to automatically install all the dependencies listed in the file. This helps ensure that anyone who wants to run your project can easily set up the required environment by installing the listed packages with their specified versions.

To install the packages listed in the requirements.txt file, you can use the following command:
pip install -r requirements.txt

This command tells pip to read the requirements.txt file and install all the listed packages and their specified versions into the current Python environment.
