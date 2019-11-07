"""
This module gathers information about active programs outside of games present
within the Steam platform. 
@author: Upquark00
"""

import win32gui

def get_active_window():
    '''Return the title of the active window as a string.'''
    active_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    return active_window

