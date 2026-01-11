from pygame.locals import *
import pygwidgets
import os, sys

# colors used for DisplayText objects and window fill
RED = (200, 10, 70)
WHITE = (255, 255, 255)

NEXT_SCENE_EVENT = USEREVENT + 1

# window and frames defined
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
FRAMES_PER_SECOND = 30

# used for time delay in play scene between rolls
ROLL_DELAY_EVENT = USEREVENT + 1  
ROLL_DELAY_TIME = 1000

# constants for different scenes
SCENE_SPLASH = 'splash'
SCENE_PLAY = 'play'
SCENE_RESULTS = 'results'

# player choice constants
EVENS = 'evens'
ODDS = 'odds'

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# sound constants
DINK_SOUND = pygwidgets.SoundEffect(resource_path('dink.wav'))
DICE_SOUND = pygwidgets.SoundEffect(resource_path('dice.wav'))
WINNER_SOUND = pygwidgets.SoundEffect(resource_path('winner.wav'))

