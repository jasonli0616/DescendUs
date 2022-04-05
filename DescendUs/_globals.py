"""
This sub-module defines global variables.

They are stored in its own module to prevent circular imports.
"""

import pygame
import os

from . import views

class Game:
    ASSETS_DIR = os.path.join('DescendUs', 'assets')

    # This variable will be overwritten with the view to render.
    # It will determine which view is currently presented.
    view = None

class Window:
    WIDTH, HEIGHT = 1000, 600
    FPS = 60

class Color:
    WHITE = (255, 255, 255)
    GRAY = (115, 115, 115)

class Font:
    pygame.font.init()

    TITLE_FONT = pygame.font.Font(os.path.join(Game.ASSETS_DIR, 'RubikGlitch-Regular.ttf'), 100)
    TEXT_FONT = pygame.font.Font(os.path.join(Game.ASSETS_DIR, 'Oswald-Light.ttf'), 30)