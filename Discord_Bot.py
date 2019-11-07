"""
First draft authored on Tues Jan 1 20:14:40 2019
Intuitive bot that checks user status across multiple digital platforms. 
@author: Upquark00
"""

import discord
import get_steam_info

# # # # # RETRIEVE STEAM INFORMATION # # # # #

steam_ID = ''
API_key = ''

''' Grab Steam player information via the Steam API using the player's known
Steam ID (which is unchanging) and your own API key (unique to each developer.)''' 
new_player = get_steam_info.Info_handler(steam_ID, API_key)
new_player_info = new_player.get_player_info()
new_player_status = new_player.get_player_status(new_player_info)
active_game = new_player.get_ingame_name(new_player_info)

# # # # # BUILD AND LAUNCH DISCORD BOT # # # # #

TOKEN = 'NTI5ODg1MTY2NzYwNjI0MTY5.XcJlaA.ZD__RCpGlFjHFNX2zvJWDxIClIY'

client = discord.Client()
      
@client.event
async def on_ready():
    '''Called automatically when client is done preparing data from Discord.
    Schedules coroutine on_ready using Task client.loop.create_task.'''
    await client.change_presence(game=discord.Game(name=active_game))
    print('The bot is ready')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message):
    # Prevents bot from responding to itself
    if message.author == client.user:
        return
    
    # Defines bot trigger and response 
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

client.run(TOKEN)