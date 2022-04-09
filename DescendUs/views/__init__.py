"""
This sub-module contains all the classes for the views/pages.

The current view is stored in a _global.py variable called view.
It can be changed anywhere in the program, and the main.py file will
display it.

The main.py will call the .show() method on each view class to display
it to the screen. Accordingly, each view class in this submodule
must have a .show() method that displays it to the screen.
"""

from .Homepage import Homepage
from .Game import Game