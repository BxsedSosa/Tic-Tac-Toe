"""Imports"""

from display import display_game, update_board
from game_logic import ask_player_position, check_for_winner_round

board = [["-"] * 3 for _ in range(3)]

while True:
    player, cpu = 0, 0

    display_game()
    player_move = ask_player_position()
    update_board(player_move)
    result = check_for_winner_round()

    if result == "player":
        player += 1
    elif result == "cpu":
        cpu += 1

    if player == 3:
        break
    elif cpu == 3:
        break
