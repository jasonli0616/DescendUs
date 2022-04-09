"""
This sub-module defines global variables.

They are stored in its own module to prevent circular imports.
"""

import pygame
import os

class Game:
    ASSETS_DIR = os.path.join(os.getcwd() ,'DescendUs', 'assets')

    # This variable will be overwritten with the view to render.
    # It will determine which view is currently presented.
    view = None

    player = None

    ammo = 10
    hp = 100
    lasers = []
    collidables = []
    km_to_earth = 1000
    won = False
    lost = False

class Window:
    WIDTH, HEIGHT = 1000, 600
    FPS = 60

class Color:
    WHITE = (255, 255, 255)
    GRAY = (115, 115, 115)
    RED = (255, 0, 0)

class Font:
    pygame.font.init()

    TITLE_FONT = pygame.font.Font(os.path.join(Game.ASSETS_DIR, 'RubikGlitch-Regular.ttf'), 100)
    TEXT_FONT = pygame.font.Font(os.path.join(Game.ASSETS_DIR, 'Oswald-Light.ttf'), 30)


class Earth:
    REGULAR_POSITION = (0, 450)
    WON_POSITION = (0, 300)

    earth = None