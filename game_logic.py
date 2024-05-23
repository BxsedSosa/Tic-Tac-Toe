"""Imports"""

import enum
from random import randint
import display

PICKS = ["x", "o"]
WINNER = [[pick] * 3 for pick in PICKS]
board = display.board


def ask_player_position() -> list:
    """Ask user for position they want to place mark"""
    x_coordinate = check_input(input("Please enter a row you want to mark:\n"))
    y_coordinate = check_input(input("Please enter a column you want to mark:\n"))
    coordinates = check_used_position([x_coordinate, y_coordinate])

    return coordinates


def get_cpu_position() -> list:
    """Get random cpu position"""
    coordinate = [randint(0, 2) for _ in range(2)]
    while board[coordinate[0]][coordinate[1]] in PICKS:
        coordinate = [randint(0, 2) for _ in range(2)]

    return coordinate


def check_input(coordinate: str) -> int:
    """Checks if input is valid from user"""
    while (
        not coordinate.isdigit()
        or len(coordinate) != 1
        or int(coordinate) not in range(1, 4)
    ):
        coordinate = input(
            "Please only enter a number inbetween 1 to 3\nExample: '1'\n"
        )

    return int(coordinate) - 1


def check_used_position(coordinates: list) -> list:
    """Check if the position is already used"""
    while board[coordinates[0]][coordinates[1]] in PICKS:
        print("Please enter a new coordinate! This coordinate is already used.")
        coordinates = ask_player_position()

    return coordinates


def check_game_winner() -> None:
    player = 0
    cpu = 0
    ties = 0

    pass


def check_who_won() -> None:
    return None


def check_for_winner_round() -> None:
    """Check board if there is a winner"""
    # if check_row(board):
    # if check_column(board):
    # if check_diagonal(board):


def check_row(grid: list) -> bool:
    """Checks board rows to determine winner"""
    for row in grid:
        if row in WINNER:
            return True

    return False


def check_column(grid: list) -> bool:
    """Retrieves column elements and checks if theres a winner"""
    columns = []

    for index1 in range(len(grid)):
        columns.append([grid[index2][index1] for index2 in range(len(grid))])

    return check_row(columns)


def check_diagonal(grid: list) -> bool:
    """Retrieves diagonal elements and checks if theres a winner"""
    diagonal = []

    diagonal.append([row][idx] for idx, row in enumerate(grid))
    diagonal.append([row][2 - idx] for idx, row in enumerate(grid))

    return check_row(diagonal)


def check_board_filled(grid: list) -> bool:
    """Check if the board is not longer playable"""
    for row in grid:
        for element in row:
            if "-" in element:
                return False

    return True
