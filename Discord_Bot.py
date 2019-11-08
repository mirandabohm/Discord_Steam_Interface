"""
First draft authored on Tues Jan 1 20:14:40 2019
Intuitive bot that checks user status across multiple digital platforms. 
@author: Upquark00
"""

import asyncio
import discord
import get_steam_info

# # # # # RETRIEVE STEAM INFORMATION # # # # #

steam_ID = 'steam_id'
API_key = 'api_key'

''' Grab Steam player information via the Steam API using the player's known
Steam ID (which is unchanging) and your own API key (unique to each developer.)''' 
new_player = get_steam_info.Info_handler(steam_ID, API_key)
new_player_info = new_player.get_player_info()
new_player_status = new_player.get_player_status(new_player_info)
active_game = new_player.get_ingame_name(new_player_info)

# # # # # BUILD AND LAUNCH DISCORD BOT # # # # #

BOT_TOKEN = 'bot_token'

client = discord.Client()

async def change_status_regularly():
    '''Instigates regular bot status updates, at an interval of 5 seconds.'''
    while True:
        await client.change_presence(game=discord.Game(name='Status 1'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='Status 2'))
        await asyncio.sleep(5)
        
@client.event
async def on_ready():
    '''Calls automatically when client is done preparing data from Discord.
    Schedules coroutine on_ready using Task client.loop.create_task.'''
    client.loop.create_task(change_status_regularly())
    print('The bot is ready')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    '''Defines in-server message which triggers bot response. Breaks function 
    if message author is bot itself'''
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

client.run(BOT_TOKEN)