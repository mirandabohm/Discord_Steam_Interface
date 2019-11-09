"""
First draft authored on Tues Jan 1 20:14:40 2019
Intuitive bot that checks user status across multiple digital platforms. 
@author: Upquark00
"""

import asyncio
import discord
import get_steam_info
import get_other_program_info
import nest_asyncio

'''Apply a patch allowing nested use of asyncio.run. 
Credit: https://github.com/erdewit/nest_asyncio'''
nest_asyncio.apply()

# # # # # DEFINE VARIABLES # # # # #

steam_ID = ''
API_key = ''
BOT_TOKEN = ''

# # # # # RETRIEVE STEAM INFORMATION # # # # #

# Grab Steam player information via the Steam API using the player's known
# Steam ID (which is unchanging) and your own API key (unique to each developer.)''' 
new_player = get_steam_info.Info_handler(steam_ID, API_key)
new_player_info = new_player.get_player_info()
new_player_status = new_player.get_player_status(new_player_info)
active_game = new_player.get_ingame_name(new_player_info)

# # # # # BUILD AND LAUNCH DISCORD BOT # # # # #

# Open a connection with the Discord client
client = discord.Client()

async def change_status_regularly() -> None:
    # Updates bot status with active window title at a specified interval.'''
    while True: 
        active_window = get_other_program_info.get_active_window()
        await client.change_presence(game=discord.Game(name=active_window))
        await asyncio.sleep(2)
        await client.change_presence(game=discord.Game(name='Something Else'))
        await asyncio.sleep(2)
        
@client.event
async def on_ready() -> None:
    # Calls automatically when client is done preparing data from Discord.
    # Schedules coroutine on_ready using Task client.loop.create_task.'''
    client.loop.create_task(change_status_regularly())
    print('The bot is ready')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
async def on_message(message) -> None:
    # Defines in-server message which triggers bot response. Breaks function 
    # if message author is bot itself'''
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
client.run(BOT_TOKEN)






