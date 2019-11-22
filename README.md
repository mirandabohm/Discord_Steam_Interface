# A Steam-Interfacing Discord Bot built for Python

This project creates bot intended to discover and displaz a Discord user's 
current activity by

(a) Checking for an active session in Steam, a major gaming platform, and importing 
details about the user's active game, if applicable. 

Status will be translated as follows: 

   STEAM STATUS        | STEAM STATE | DISCORD STATUS
   'Offline'           |      0      | 'Offline'
   'Online'            |      1      | 'Online'
   'Busy'              |      2      | 'dnd'
   'Away'              |      3      | 'Idle'
   'Snooze'            |      4      | 'Idle'
   'Looking to trade'  |      5      | 'Online'
   'Looking to play'   |      6      | 'Online'

(b) If no active Steam session is found, information about the user's currently 
active window will be returned instead. 

### Requirements
    
    (0) A system which runs Python
	
	(1) Discord.py (see below)
    
	(2) a Steam ID, obtainable via the Steam client under View > Settings. 
	
	(3) a Steam API Key, which can be found here: 
    	https://steamcommunity.com/dev/apikey
    	
	(4) a Discord bot token, which can be created in the Discord Developer portal: 
    	https://discordapp.com/developers/applications/
		
### Check Dependencies 

To check for Python on your system, enter `python --version` into the command line. 
A response such as `Python 2.7.16` indicates proper installaiton. A result such as 
`'python' is not recognized as an internal or external command, operable program, or batch file'` 
implies the need for installation or re-installlation. 

To install the Discord.py library, enter the following: 
`py -3 -m pip install -U discord.py`