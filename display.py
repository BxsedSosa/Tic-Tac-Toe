"""Imports"""

from os import system
from pyfiglet import Figlet

BORDER = "=" * 65
logo_font = Figlet(font="larry3d")
game_font = Figlet(font="banner")


def clear_console() -> None:
    """Clear console from text"""
    system("clear||cls")
