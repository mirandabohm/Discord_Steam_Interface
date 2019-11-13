'''
This module imports information from a Steam user's session.

Annotated on 11/10/2019 @ 14:20:00 PDT 
Author: Upquark00

'''

import requests

from credentials import API_key, steam_ID, BOT_TOKEN

class SteamUser():
    '''Create an object holding a player's account information and current status.'''
    
    def __init__(self, steam_ID, API_key):
        self.API_url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=' \
        + API_key +'&steamids=' + steam_ID
        self.info = self.get_user_info()
        self.active_game = self.get_active_game(self.info) 
        self.name = self.info['personaname']
        self.steam_state = self.get_steam_state(self.info)
        self.discord_status = self.get_player_discord_status(self.steam_state)
        self.profile_url = 'https://steamcommunity.com/profiles/' + steam_ID
        
    def get_user_info(self):
        '''Returns a dict containing Steam information for one player using the
        Steam API. Requires the desired player's user ID and a valid API key.'''
        response = requests.get(self.API_url)
        
        if response.status_code != 200:
            raise Exception('Request unsuccessful; returned code ' + str(response.status_code) \
            + ': ' + str(requests.status_codes._codes[response.status_code][0]))
        else:
            print('Success! API responded to call.')
            player_info = response.json()['response']['players'][0]
        return player_info

# NOTE: get_player_discord_status translates the Steam status given by the Steam
# API to a Discord status readable by the Bot. That functionality shoudl be 
# appropriately divided such that a function in this module returns steam status, 
# and another, separate function in Dicord_Bot.py translates this to a Discrd status. 

# TODO: define a function get_steam_state which takes the player's info dict
# and returns the steam state for export to get_discord_status. Should this be 
# returned as steam state or as steam status??
    
    def get_steam_state(self, player_info_dict):
        '''Grabs Steam status from information provided by the Steam API. 
        
        Accepts JSON information provided by the Steam API as a dictionary and 
        returns Steam State as a number between 0 and 6:
        
        'Offline'           |      0      | 'Offline'
        'Online'            |      1      | 'Online'
        'Busy'              |      2      | 'dnd'
        'Away'              |      3      | 'Idle'
        'Snooze'            |      4      | 'Idle'
        'Looking to trade'  |      5      | 'Online'
        'Looking to play'   |      6      | 'Online'
        
        '''
        steam_state = player_info_dict['personastate']
        return steam_state
    
    def get_player_discord_status(self, steam_state):
        
        '''Translates player's Steam status to its corresponding Discord status.
        
        Takes Steam user's information as a dictionary, extracts steam status 
        code (as a number 0 through 6), and returns Discord status as a string.
        
        STEAM STATUS        | STEAM STATE | DISCORD STATUS

        
        '''

        possible_discord_statuses = {0: 'offline', 1: 'online', 3: 'dnd', 4: 'idle', 5: 'idle', 6: 'online', 7: 'online'}
        discord_status = possible_discord_statuses[steam_state]
        return discord_status
        
    def get_active_game(self, player_info_dict):
        '''Returns the name of the Steam game that the player is currently playing. 
        If not currently playing anything, return False.'''
        
        try:
            self.__game = player_info_dict['gameextrainfo']
            game_name = self.__game
        except KeyError:  
            game_name = False
        return game_name 
    
print(API_key, steam_ID, BOT_TOKEN)
player = SteamUser(steam_ID, API_key)
