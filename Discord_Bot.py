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

'''Apply a patch allowing nested use of asyncio.run. 
Credit: https://github.com/erdewit/nest_asyncio'''
nest_asyncio.apply()

# # # # # DEFINE VARIABLES # # # # #

steam_ID = '76561198887030405'
API_key = '7C5B5B1A3F0031E78315327C1EB7BA57'
BOT_TOKEN = 'NTI5ODg1MTY2NzYwNjI0MTY5.XcJlaA.ZD__RCpGlFjHFNX2zvJWDxIClIY'

# # # # # RETRIEVE STEAM INFORMATION # # # # #

# Grab Steam player information via the Steam API using the player's known
# Steam ID (which is unchanging) and your own API key (unique to each developer.)''' 
new_player = get_steam_info.Info_handler(steam_ID, API_key)
new_player_info = new_player.get_player_info()
new_player_status = new_player.get_player_status(new_player_info)
active_game = new_player.get_ingame_name(new_player_info)

class Bot(): 
    '''This class brings a Discord bot online using the Discord API.'''
    client = discord.Client()
    
    def __init__(self):
        pass 
    
    async def update_status(self) -> None:
        '''Updates bot status with active window title at a specified interval.'''
        while True: 
            active_window = get_other_program_info.get_active_window()
            await self.client.change_presence(game=discord.Game(name=active_window))
            await asyncio.sleep(2)
            await self.client.change_presence(game=discord.Game(name='Something Else.'))
            await asyncio.sleep(2)
            
    @client.event
    async def on_ready() -> None:
        '''Schedules the coroutine on_ready when client is done preparing data from Discord.'''
        # self.client.loop.create_task(self.update_status())
        print('The bot is ready')
        print('Logged in as')
        # print(client.user.name)
        # print(client.user.id)
        print('------')
        
    @client.event
    async def on_message(self, message) -> None:
        # Defines in-server message which triggers bot response. Breaks function 
        # if message author is bot itself'''
        if message.author == self.client.user:
            return
    
        if message.content.startswith('!hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await self.client.send_message(message.channel, msg)
        
myBot = Bot()
Bot.client.run(BOT_TOKEN)






