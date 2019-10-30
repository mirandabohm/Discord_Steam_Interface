# Discord_Steam_Interface

This project finds a Discord user's current activity and presents their status on this platform accordingly. 

This is to include either the name of the active window running, or the name of the game currently being played on Steam. This name will then be displayed by a bot which can be incorporated into a player's active server. 

Note, successful operation requires: 
	(1) a Steam ID, obtainable through the player's Steam profile
	(2) a Steam API Key, which can be found in developer tools. 
	(3) a bot token

Additionally, if player is registered on Steam, their activity status will be translated as follows: 

   STEAM STATUS        | STEAM STATE | DISCORD STATUS
   'Offline'           |      0      | 'Offline'
   'Online'            |      1      | 'Online'
   'Busy'              |      2      | 'dnd'
   'Away'              |      3      | 'Idle'
   'Snooze'            |      4      | 'Idle'
   'Looking to trade'  |      5      | 'Online'
   'Looking to play'   |      6      | 'Online'

