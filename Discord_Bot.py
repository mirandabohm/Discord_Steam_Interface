"""
First draft authored on Tues Jan 1 20:14:40 2019
Intuitive bot that checks user status across multiple digital platforms. 
@author: Upquark00
"""

import asyncio

import discord
import nest_asyncio

import get_steam_info
import get_other_program_info
from credentials import API_key, steam_ID, BOT_TOKEN

'''Apply a patch allowing nested use of asyncio.run. 
Credit: https://github.com/erdewit/nest_asyncio'''
nest_asyncio.apply()


# # # # # RETRIEVE STEAM INFORMATION # # # # #
def get_activity():
    steam_player = get_steam_info.SteamUser(steam_ID, API_key)
    if steam_player.active_game:
        activity = steam_player.active_game
    else:
        activity = get_other_program_info.get_active_window()
    return activity

# Bring a Discord bot online using the Discord API.'''
client = discord.Client()

async def update_status() -> None:
    '''Updates bot status with active window title at a specified interval.'''
    while True: 
        await client.change_presence(game=discord.Game(name=get_activity()))
        await asyncio.sleep(2)
        await client.change_presence(game=discord.Game(name='Something Else.'))
        await asyncio.sleep(2)
        
@client.event
async def on_ready() -> None:
    '''Schedules the coroutine on_ready when client is done preparing data from Discord.'''
    client.loop.create_task(update_status())
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




