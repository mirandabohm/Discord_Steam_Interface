"""
First draft authored on Tues Jan 1 20:14:40 2019
Intuitive bot that checks user status across multiple digital platforms. 
@author: Upquark00
"""

import time
import win32gui
import psutil
import subprocess
import discord
import asyncio
import get_steam_info

class Bot_handler():
    
    # Define the Client object for this session.
    client = discord.Client()
    
    def __init__(self, program_name, steam_id, api_key, bot_token):
        self.program_name = program_name
        self.process = self.program_name + '.exe'
        self.__program_running = self.get_program_running(self.process)
        self.__STEAM_ID = STEAM_ID
        self.__API_KEY = API_KEY
        self.__BOT_TOKEN = BOT_TOKEN
        
    def get_program_running(self, process_str):
        '''Determine whether the specified process_str is running.'''
        if process_str in (process.name() for process in psutil.process_iter()):
            self.__program_running = True
            print(self.program_name,"is currently running.")
        else:
            self.__program_running = False
            print(self.program_name,"is not currently running.")
        return self.__program_running
    
    @client.event
    async def on_ready(self):
        '''Called automatically when client is done preparing data from Discord.
        Schedules coroutine on_ready using Task client.loop.create_task.'''
        self.__client.loop.create_task(self.status_task())
        print('Logged in as')
        print(self.__client.user.name)
        print(self.__client.user.id)
        print('------')
    
    async def status_task(self):
        while True:
            if self.__program_running:
                self.__player_info = get_steam_info.get_player_info(self.__API_KEY, self.__STEAM_ID)
                self.__player_status = get_steam_info.get_player_status(self.__player_info)
                self.__ingame = get_steam_info.get_ingame_name(self.__player_info)
                
                if self.__ingame:
                    await self.__client.change_presence(status = discord.Status.online, game = discord.Game(name = str(self.__ingame)), afk=False)
                    await asyncio.sleep(3)
                else:
                    await self.__client.change_presence(status = discord.Status.dnd, game = discord.Game(name = 'nothing at the moment'))
                    await asyncio.sleep(3)
            else:
                self.get_active_window()
            
    def get_active_window(self):
        '''Return the title of the active window as a string.'''
        self.__active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        return self.__active_window    

'''
    def run_the_bot(self):
        # Activates the bot.
        discord.Client.run(self.__BOT_TOKEN)
''' 

PROGRAM_NAME = 'Steam'
STEAM_ID = ''
API_KEY = ''
BOT_TOKEN = ''       
b = Bot_handler(PROGRAM_NAME, STEAM_ID, API_KEY, BOT_TOKEN)
# b.run_the_bot()
