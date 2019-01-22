"""
Created on Tues Jan 1 20:14:40 2019
Intuitive bot that checks user status across multiple digital platforms. 
@author: Upquark00
"""

import time
import win32gui as w
import psutil as ps
import subprocess as sp
import discord as ds
import asyncio
import get_steam_info as gs

class Bot_handler():
    def __init__(self, program_name = 'Steam',
                 STEAM_ID = 'XXXXXXXXXXXXXXXXXX',
                 API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                 BOT_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'):
        self.__client = ds.Client()
        self.program_name = program_name
        self.process = self.program_name + '.exe'
        self.__program_running = self.get_program_running(self.process)
        
        self.__STEAM_ID = STEAM_ID
        self.__API_KEY = API_KEY
        self.__BOT_TOKEN = BOT_TOKEN
        
    def get_program_running(self, process_str):
        '''Determine whether the specified process_str is running.'''
        if process_str in (proc.name() for proc in ps.process_iter()):
            self.__program_running = True
            print(self.program_name,"is currently running.")
        else:
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
                self.__player_info = gs.get_player_info(self.__API_KEY, self.__STEAM_ID)
                self.__player_status = gs.get_player_status(self.__player_info)
                self.__ingame = gs.get_ingame_name(self.__player_info)
                
                if self.__ingame:
                    await self.__client.change_presence(status = ds.Status.online, game = ds.Game(name = str(self.__ingame)), afk=False)
                    await asyncio.sleep(3)
                else:
                    await self.__client.change_presence(status = ds.Status.dnd, game = ds.Game(name = 'nothing at the moment'))
                    await asyncio.sleep(3)
            else:
                self.get_active_window()
            
    def get_active_window(self):
        '''Return the title of the active window as a string.'''
        self.__active_window = w.GetWindowText(w.GetForegroundWindow())
        return self.__active_window    

    def run_bot(self):
        '''Activates the bot.'''
        self.__client.run(self.__BOT_TOKEN)
        
b = Bot_handler()


