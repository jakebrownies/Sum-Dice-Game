# Jacob Brown
# 2/28/2025
# COP5230.701S25
# Module 7 Assignment
# Sum of Dice Game

# all necessary modules imported including the three scenes and constants file
import pygame
from pygame.locals import *
import pyghelpers

from SceneSplash import *
from ScenePlay import *
from SceneResults import *
from constants import *

# pygame initialized, window created, and clock started
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dice Game")
clock = pygame.time.Clock()

# lsit of scenes created for SceneMgr to use, SceneMgr initialized to manage the 3 scenes of the game
sceneList = [SceneSplash(window), ScenePlay(window), SceneResults(window)]
oSceneMgr = pyghelpers.SceneMgr(sceneList, FRAMES_PER_SECOND)
oSceneMgr.run()

# display is updated at 30 frames per second
pygame.display.update()
clock.tick(FRAMES_PER_SECOND)