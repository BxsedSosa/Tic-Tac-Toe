"""Imports"""

from random import randint
import display
from game_logic import check_for_winner, check_for_tie
from validation import check_already_used_position, check_input_is_valid

game_board = [["-"] * 3 for _ in range(3)]


def reset_board() -> list:
    """Resets game board"""
    return [["-"] * 3 for _ in range(3)]


def ask_try_again(answer) -> bool:
    """Asks user to try again"""
    return answer in ["y", "yes"]


def get_user_mark_position() -> list:
    """Gets players position and checks if position is already used"""

    def ask_user_for_position(description: str) -> str:
        """Ask user for posiition and validates it"""
        user_input = input(f"Please enter {description}:\n")

        while check_input_is_valid(user_input):
            user_input = input(
                f"Please enter valid {description}:\nValid {description}'s are: '1', '2', or '3'\n"
            )
        return user_input

    x_coor = ask_user_for_position("row")
    y_coor = ask_user_for_position("column")
    user_coor = [int(x_coor) - 1, int(y_coor) - 1]

    while check_already_used_position(game_board, user_coor):
        print("Those coodindates are already used!\nPlease enter in new coodindates")
        x_coor = ask_user_for_position("row")
        y_coor = ask_user_for_position("column")
        user_coor = [int(x_coor) - 1, int(y_coor) - 1]

    return user_coor


def get_cpu_mark_position() -> list:
    """Gets random position from cpu"""
    cpu_move = [randint(0, 2), randint(0, 2)]

    while check_already_used_position(game_board, cpu_move):
        cpu_move = [randint(0, 2), randint(0, 2)]

    return cpu_move


def check_end_game() -> bool:
    """Checks if user wants to end the program"""
    display.display_try_again()
    another_try = input()

    if ask_try_again(another_try):
        return False

    display.display_end()
    return True


def main(grid) -> None:
    """Main function"""
    display.display_welcome_screen()

    player_score, cpu_score, moves = 0, 0, 0
    game_round = 1

    while player_score < 3 and cpu_score < 3:
        display.display_game(grid, player_score, cpu_score, game_round)
        user_coor = get_user_mark_position()
        grid[user_coor[0]][user_coor[1]] = "x"
        moves += 1

        if check_for_winner(grid):
            moves = 0
            player_score += 1
            display.display_game(grid, player_score, cpu_score, game_round)
            display.display_round_winner("Player")

            if player_score == 3:
                if check_end_game():
                    break

                player_score, cpu_score, moves = 0, 0, 0
                game_round = 1

            game_round += 1
            grid = reset_board()

        elif check_for_tie(moves):
            moves = 0
            game_round += 1
            display.display_tie()
            grid = reset_board()

        display.display_game(grid, player_score, cpu_score, game_round)
        cpu_coor = get_cpu_mark_position()
        grid[cpu_coor[0]][cpu_coor[1]] = "o"
        moves += 1

        if check_for_winner(grid):
            moves = 0
            cpu_score += 1
            display.display_game(grid, player_score, cpu_score, game_round)
            display.display_round_winner("Cpu")

            if player_score == 3:
                if check_end_game():
                    break

                player_score, cpu_score, moves = 0, 0, 0
                game_round = 1

            game_round += 1
            grid = reset_board()

        elif check_for_tie(moves):
            moves = 0
            game_round += 1
            display.display_tie()
            grid = reset_board()


main(game_board)
