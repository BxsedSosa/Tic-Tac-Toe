"""Imports"""

from os import system
from pyfiglet import Figlet

BORDER = "=" * 65
logo_font = Figlet(font="larry3d")
game_font = Figlet(font="banner")
board = [["-"] * 3 for _ in range(3)]


def clear_console() -> None:
    """Clear console from text"""
    system("clear||cls")


def display_logo() -> None:
    """Display Tic Tac Toe Logo"""
    print(logo_font.renderText("TicTacToe"))
    print(BORDER)


def display_map() -> None:
    """Display game board"""
    for row in board:
        print("  ".join(game_font.renderText(row)))


def display_start() -> None:
    """Display Start of the game"""
    clear_console()
    display_logo()
    display_map()


def update_display(coordinates: list, mark: str) -> None:
    """Display board continuously"""
    clear_console()
    display_logo()
    board[coordinates[0]][coordinates[1]] = mark
    display_map()
