# LinkedInBot
A simple LinkedInBot using Python and Selenium

The purpose of the bot is to visit profiles in your LinkedIn's "suggested contacts" list. The bot goes to "Your Network", picks a profile at random and visits it. It then comes back to "Your Network", picks another profile and repeats the process. In LinkedIn, whenever you visit a profile, that person gets a notification that you visited. Therefore, visiting more profiles gives you more visibility, which could potentially result in more people noticing you and in the development of more connections.

The bot is able to open a Chrome window, log in to LinkedIn using your credentials, go to your network in the top menu, and visit the profile of a person in your "recommended contacts" section.



Instructions: Chrome's webdriver (can be downloaded from https://chromedriver.chromium.org/downloads) Change the variable webdriver_path in LinkedinBot.py to the path where you installed the webdriver Edit the username and password variables in linkedin_login.py and replace them with your login credentials (email and password).

Notes: Because Selenium access the xpath of the web elements, and because certain xpaths in the program access the text of the elements, this bot will run better in the Spanish version of Linkedin. However, the main functionality remains unaffected. For better performance it is recommended to run the LinkedinBot.py file on a terminal in interactive mode (cd to the file´s directory and type python -i LinkedinBot.py) Once you run the program in interactive mode, a new window will open. If you have Linkedin in Spanish, type bot.login() in the terminal. Then the bot will log in and you'll see a bunch of popups. If you don't have Linkedin in Spanish, you can login manually and once you're in, type bot.click_on_profiles() in the terminal.

Have fun!

""" THIS PROGRAM IS ONLY FOR DEMOSTRATION PURPOSES AND NOT TO BE USED AGAINST LINKEDIN´S TERMS OF SERVICE """
