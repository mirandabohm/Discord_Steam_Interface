"""
Created on Tues Jan 1 20:14:40 2019
Attempt at making Discord Bot for changing online status automatically. 
@author: Upquark00
"""

import psutil as ps
import discord as ds
import asyncio


# =============================================================================
# PART I: Determines the nature of programs running on your machine. 
# =============================================================================

PROGRAM_NAME = 'Steam'
PROCESS = PROGRAM_NAME + '.exe'

if PROCESS in (proc.name() for proc in ps.process_iter()):
    steam_running = True
    print(PROGRAM_NAME,"is currently running.")
else:
    steam_running = False
    print(PROGRAM_NAME,"is not currently running.")

bot_token = ''

# =============================================================================
# If Steam is running, fetch data on Steam session. 
# =============================================================================


# =============================================================================
# PART II: The BOT
# =============================================================================

game_name = 'GAME NAME' 
client = ds.Client()

@client.event
async def on_ready():
    '''Client done preparing data received from discord'''
    client.loop.create_task(status_task())
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

async def status_task():
    while True:
        await client.change_presence(status = ds.Status.offline, game = ds.Game(name = "XXXXX"), afk=False)
        await asyncio.sleep(3)
        await client.change_presence(status = ds.Status.idle, game = ds.Game(name = game_name), afk=False)
        await asyncio.sleep(3)
        
client.run(bot_token)









