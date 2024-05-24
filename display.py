"""Imports"""

from os import system
from pyfiglet import Figlet

BORDER = "=" * 65
logo_font = Figlet(font="larry3d")
game_font = Figlet(font="banner")
game_board = [["-"] * 3 for _ in range(3)]


def clear_console() -> None:
    """Clear console from text"""
    system("clear||cls")


def display_logo() -> None:
    print(logo_font.renderText("TicTacToe"))
    print(BORDER)


def display_grid(grid) -> None:
    for row in grid:
        print("  ".join(game_font.renderText(row)))


def display_game() -> None:
    display_logo()
    display_grid(game_board)
