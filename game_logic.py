"""Imports"""

from random import randint
from display import board, display_game

PICKS = ["x", "o"]
WINNER = [[pick] * 3 for pick in PICKS]


# Positions for the board
def ask_player_position() -> list:
    """Ask user for position they want to place mark"""
    x_coordinate = check_input(input("Please enter a row you want to mark:\n"))
    display_game()
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
        display_game()
        coordinate = input(
            "Please only enter a number inbetween 1 to 3\nExample: '1'\n"
        )

    return int(coordinate) - 1


def check_used_position(coordinates: list) -> list:
    """Check if the position is already used"""
    while board[coordinates[0]][coordinates[1]] in PICKS:
        display_game()
        print("Please enter a new coordinate! This coordinate is already used.")
        coordinates = ask_player_position()

    return coordinates


# Check for a 3 in a row
def check_for_winner_round() -> str:
    """Check board if there is a winner"""
    display_game()
    if check_row(board):
        return "player" if check_row(board) == "x" else "cpu"
    if check_column(board):
        return "player" if check_column(board) == "x" else "cpu"
    if check_diagonal(board):
        return "player" if check_diagonal(board) == "x" else "cpu"

    return ""


def check_row(grid: list) -> str:
    """Checks board rows to determine winner"""
    for row in grid:
        if row in WINNER:
            return row[0]

    return ""


def check_column(grid: list) -> str:
    """Retrieves column elements and checks if theres a winner"""
    columns = []

    for index1 in range(len(grid)):
        columns.append([grid[index2][index1] for index2 in range(len(grid))])

    return check_row(columns)


def check_diagonal(grid: list) -> str:
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
