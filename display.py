"""Imports"""

from os import system
from main import board
from pyfiglet import Figlet

BORDER = "=" * 65
logo_font = Figlet(font="larry3d")
game_font = Figlet(font="banner")


def clear_console() -> None:
    """Clear console from text"""
    system("clear||cls")


def display_wins() -> None:
    """Displays win from player and cpu"""
    print("Best of 3       Player 1: 0 | Cpu: 0       Game: 1".center(len(BORDER)))


def display_logo() -> None:
    """Display Tic Tac Toe Logo"""
    print(logo_font.renderText("TicTacToe"))
    display_wins()
    print(BORDER)


def display_map() -> None:
    """Display game board"""
    for row in board:
        print("  ".join(game_font.renderText(row)))


def update_board(coor: list) -> None:
    board[coor[0]][coor[1]] = "x"


def display_game() -> None:
    """Display board continuously"""
    clear_console()
    display_logo()
    display_map()
