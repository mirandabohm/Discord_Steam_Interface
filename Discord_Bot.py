"""
First draft authored on Tues Jan 1 20:14:40 2019
Intuitive bot that checks user status across multiple digital platforms. 
@author: Upquark00
"""

import asyncio

import discord
import nest_asyncio

import get_other_program_info
from get_steam_info import steam_player
from credentials import BOT_TOKEN

# Apply a patch allowing nested use of asyncio.run. 
# Credit: https://github.com/erdewit/nest_asyncio'''
nest_asyncio.apply()

# Bring a Discord bot online using the Discord API.'''
client = discord.Client()

# TODO: add tests

class DiscordUser():
    '''Stores pertinent Discord-side information for a user. Will run a bot, later.''' 
    
    def __init__(self):
        self.activity = self.get_activity(steam_player)
        self.discord_status = self.get_player_discord_status(steam_player.get_steam_state(steam_player.info))
        
    def get_activity(self, player: object) -> str:
        '''Grab info from user's currently active session, and set current activity.
        
        If user is currently active on Steam, determine whether user is actively 
        engaged in a game. If so, set this to current activity. If not, set current
        activity to title of active OS window.'''
        
        if player.active_game:
            activity = player.active_game
        else:
            activity = get_other_program_info.get_active_window()
        return activity
    
    def get_player_discord_status(self, steam_state: int) -> str:
        
        '''Translates player's Steam status to its corresponding Discord status.
        
        Does this by accepting Steam state as a value between 0 and 6, and finding
        its corresponding Discord status according to this table:
        
        STEAM STATUS        | STEAM STATE | DISCORD STATUS
        'Offline'           |      0      | 'Offline'
        'Online'            |      1      | 'Online'
        'Busy'              |      2      | 'dnd'
        'Away'              |      3      | 'Idle'
        'Snooze'            |      4      | 'Idle'
        'Looking to trade'  |      5      | 'Online'
        'Looking to play'   |      6      | 'Online'
        
        '''
        possible_discord_statuses = {0: 'offline', 1: 'online', 3: 'dnd', 4: 'idle', 5: 'idle', 6: 'online', 7: 'online'}
        discord_status = possible_discord_statuses[steam_state]
        return discord_status

D = DiscordUser()

async def update_status() -> None:
    '''Updates bot status with active window title at a specified interval.'''
    while True: 
        await client.change_presence(game=discord.Game(name=D.get_activity(steam_player)), status=discord.Status('idle'))
        await asyncio.sleep(2)
        await client.change_presence(game=discord.Game(name='Snarky Comment Here'), status=discord.Status('dnd'))
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
async def on_message(message: object) -> None:
    '''Defines in-server message which triggers bot response. Breaks function 
    if message author is bot itself'''
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

client.run(BOT_TOKEN)







