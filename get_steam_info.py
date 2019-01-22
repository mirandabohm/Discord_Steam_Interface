
import requests

class Info_handler():
    '''Keep track of a player's information in real time.'''
    def __init__(self, steam_ID = 'XXXXXXXXXXXXXXX', 
                 API_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'):
        
        self.__steam_ID = steam_ID
        self.__API_key = API_key        
        self.__API_url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=' \
        + self.__API_key +'&steamids=' + self.__steam_ID
        self.statuslist = {0: 'offline', 1: 'online', 3: 'dnd', 4: 'idle', 5: 'idle', 6: 'online', 7: 'online'}
        # call status

        # profile_url = 'https://steamcommunity.com/profiles/' + steam_ID
        
        self.__player_info = self.get_player_info()
        self.__player_status = self.get_player_status(self.__player_info)
        
    def get_player_info(self):
        '''Returns a dict containing Steam information for one player using the
        Steam API. Requires the desired player's user ID and a valid API key.'''
        self.response = requests.get(self.__API_url)
        
        if self.response.status_code != 200:
            raise Exception('Request unsuccessful; returned code ' + str(self.response.status_code) \
            + ': ' + str(requests.status_codes._codes[self.response.status_code][0]))
        else:
            print('Success! API responded to call.')
            self.__player_info = self.response.json()['response']['players'][0]
        return self.__player_info
    
    def get_player_status(self, player_info_dict):
        '''Returns the player's Steam status as a Discord status type.
        
        STEAM STATUS        | STEAM STATE | DISCORD STATUS
        'Offline'           |      0      | 'Offline'
        'Online'            |      1      | 'Online'
        'Busy'              |      2      | 'dnd'
        'Away'              |      3      | 'Idle'
        'Snooze'            |      4      | 'Idle'
        'Looking to trade'  |      5      | 'Online'
        'Looking to play'   |      6      | 'Online'
        '''
        self.__steam_state = player_info_dict['personastate']
        
        self.__player_status = self.statuslist[self.__steam_state]
        return self.__player_status

# Is it better to use 'self.__steam_state' since when this variable will never 
# called outside the function? Or shall I use simply 'steam_state?'
        
    def get_ingame_name(self, player_info_dict):
        '''Returns the name of the Steam game player is playing. 
        If player is logged into Steam, but not currently playing anything,
        return False.'''
        self.__player_name = player_info_dict['personaname']
        try:
            self.__game = player_info_dict['gameextrainfo']
            print('Player ',self.__player_name,' is playing ',self.__game,'.',sep='')
            return self.__game
        except KeyError:  
            print('Player',self.__player_name,'is not currently in a game.')
            return False
    
    def get_player_name(self):
        return self.__player_name

instance = Info_handler()
info = instance.get_player_info()
print(info)
status = instance.get_player_status(info)
print(status)
game = instance.get_ingame_name(info)
print(game)