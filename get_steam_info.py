
import requests

steam_ID = 'XXXXXXXXXXXXXXX'
API_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
profile_url = 'https://steamcommunity.com/profiles/' + steam_ID

def get_player_info(API_key, steam_ID):
    url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key=' \
    + API_key +'&steamids=' + steam_ID

    resp = requests.get(url)
    
    if resp.status_code != 200:
        raise Exception('Request unsuccessful; returned code ' + str(resp.status_code) \
        + ': ' + str(requests.status_codes._codes[resp.status_code][0]))
    else:
        print('Success! API responded to call.')
        player_info = resp.json()['response']['players'][0]
    return player_info

def get_status(player_info):
    # personastate determines player's online status
    if player_info['personastate'] == 0:
        player_status = 'Offline'
    elif player_info['personastate'] == 1:
        player_status = 'Online'
    elif player_info['personastate'] == 2:
        player_status = 'Busy'
    elif player_info['personastate'] == 3:
        player_status = 'Away'
    elif player_info['personastate'] == 4:
        player_status = 'Snooze'
    elif player_info['personastate'] == 5:
        player_status = 'Looking to trade'
    elif player_info['personastate'] == 6:
        player_status = 'Looking to play'
    return player_status

def get_ingame_name(player_info):
    player_name = player_info['personaname']
    try:
        game = player_info['gameextrainfo']
        return game
    except KeyError:  
        print('Player',player_name,'is not currently in a game.')
        return False
        
player_info = get_player_info(API_key, steam_ID)
ingame_name = get_ingame_name(player_info)
