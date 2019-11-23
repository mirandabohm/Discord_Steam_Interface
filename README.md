# A Steam-Interfacing Discord Bot built in Python #

This is the Python version of the Discord Bot found here:  
[Discord_Steam_Interface Bot (Node.js edition)](https://github.com/upquark00/Discord_Steam_Interface)

This project creates a bot intended to discover and display a Discord user's 
current activity by

(a) Checking for an active session in Steam, a major gaming platform, and importing 
details about the user's active game, if applicable. 

Status will be translated as follows: 

| STEAM STATUS | STEAM STATE | DISCORD STATUS |
   |-----------|:-----------:|-----------:| 
   'Offline'           |      0      | 'Offline'
   'Online'            |      1      | 'Online'
   'Busy'              |      2      | 'dnd'
   'Away'              |      3      | 'Idle'
   'Snooze'            |      4      | 'Idle'
   'Looking to trade'  |      5      | 'Online'
   'Looking to play'   |      6      | 'Online'

(b) If no active Steam session is found, information about the user's currently 
active window will be returned instead. 

### Requirements ###
    
(0) Python 3.5 or higher

(1) Discord.py

(2) A Steam account. Create here: [https://store.steampowered.com/join](https://store.steampowered.com/join) 

(3) a Steam ID, obtainable only after a Steam account is created. Go here to create a Steam account: 
     After account creation, follow instructions here to find the assigned Steam ID: https://support.steampowered.com/kb_article.php?ref=1558-QYAX-1965
    
(4) a Steam API Key. Note that at least $5.00 USD must be spent on Steam before a key can be generated. 
   https://steamcommunity.com/dev/apikey

Note: the API key be viewed in the Steam client under View > Settings. Download the client here: 
    https://store.steampowered.com/about/
    
(5) a Discord bot token, which can be created in the Discord Developer portal: 
    https://discordapp.com/developers/applications/

### Preparation ###
In order to run the bot, a Discord server must be created. Follow the instructions here to create a server: 
  https://support.discordapp.com/hc/en-us/articles/204849977-How-do-I-create-a-server-  
  
A bot "application" must be created to run our session. Follow the instructions here: 
  https://discordpy.readthedocs.io/en/latest/discord.html
  
### Installation ###

To check for Python on your system, enter `python --version` into the command line. 
A response such as `Python 2.7.16` indicates proper installaiton. A result such as 
`'python' is not recognized as an internal or external command, operable program, or batch file'` 
implies the need for installation or re-installlation. 

To install the Discord.py library, enter the following: 
`py -3 -m pip install -U discord.py`

### Usage ### 
