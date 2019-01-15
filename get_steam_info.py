
import requests

steam_IDs = 'XXXXXXXXXXXXXXX'
API_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key='+ API_key +'&steamids=' + steam_IDs

resp = requests.get(url)

if resp.status_code != 200:
    raise Exception('Request unsuccessful; returned code ' + str(resp.status_code) + ': ' +
                    str(requests.status_codes._codes[resp.status_code][0]))
else:
    print('Success!')
    player_info = resp.json()['response']['players'][0]
    
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
