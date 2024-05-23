"""Imports"""

from game_logic import check_game_winner, ask_player_position, get_cpu_position
from display import update_display, display_start


def game_loop():
    """Starts up the game"""
    display_start()

    while check_game_winner():
        update_display(ask_player_position(), "x")
        update_display(get_cpu_position(), "o")


game_loop()
