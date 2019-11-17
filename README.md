# Discord_Steam_Interface

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
 
	(1) a Steam ID, obtainable via the Steam client under View > Settings. 
	
	(2) a Steam API Key, which can be found here: 
    	https://steamcommunity.com/dev/apikey
    	
	(3) a Discord bot token, which can be created in the Discord Developer portal: 
    	https://discordapp.com/developers/applications/
