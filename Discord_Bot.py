"""
Created on Tues Jan 1 20:14:40 2019
Intuitive bot that checks status on multiple digital platforms. 
@author: Upquark00
"""

import time
import win32gui as w
import psutil as ps
import subprocess as sp
import discord as ds
import asyncio
import get_steam_info as gs

BOT_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
STEAM_ID = 'XXXXXXXXXXXXXXX'
API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

# =============================================================================
# PART I: Determines the nature of programs running on your machine. 
# =============================================================================

PROGRAM_NAME = 'Steam'
PROCESS = PROGRAM_NAME + '.exe'

def check_steam_running():
    if PROCESS in (proc.name() for proc in ps.process_iter()):
        steam_running = True
        print(PROGRAM_NAME,"is currently running.")
    else:
        steam_running = False
        print(PROGRAM_NAME,"is not currently running.")
    return steam_running

# =============================================================================
# If Steam is running, fetch data on Steam session. 
# =============================================================================

client = ds.Client()

@client.event
async def on_ready():
    '''Performed when client done preparing data received from Discord'''
    client.loop.create_task(status_task())
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def status_task():
    while True:
        if check_steam_running():
            player_info = gs.get_player_info(API_KEY, STEAM_ID)
            # Functionality to be added later
            # player_status = gs.get_status(player_info)
            ingame_name = gs.get_ingame_name(player_info)
            
            if ingame_name:
                await client.change_presence(status = ds.Status.online, game = ds.Game(name = str(ingame_name)), afk=False)
                await asyncio.sleep(3)
            else:
                await client.change_presence(status = ds.Status.online, game = ds.Game(name = 'nothing at the moment'), afk=False)
                await asyncio.sleep(3)
        
client.run(BOT_TOKEN)



# =============================================================================
# For later
# 
# import time
# 
# running = []
# 
# i = 0
# while i <10:
#     prog = w.GetWindowText(w.GetForegroundWindow())
#     print(prog, time.time())
#     time.sleep(2)
#     running.append(prog)    
#     i += 1
# 
# =============================================================================




