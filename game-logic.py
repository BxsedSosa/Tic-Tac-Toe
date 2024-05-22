from random import randint
import display

PICKS = ["X", "O"]
WINNER = [[pick] * 3 for pick in PICKS]
BOARD = display.map


def ask_player_position() -> list:
    """Ask user for position they want to place mark"""
    x_coordinate = check_input(input("Please enter a row you want to mark:\n"))
    y_coordinate = check_input(input("Please enter a column you want to mark:\n"))
    coordinates = [x_coordinate, y_coordinate]

    return coordinates


def check_input(coordinate: str) -> int:
    """Checks if input is valid from user"""
    while (
        not coordinate.isdigit()
        or len(coordinate) != 1
        or int(coordinate) not in list(range(1, 4))
    ):
        coordinate = input(
            "Please only enter a number inbetween 1 to 3\nExample: '1'\n"
        )

    return int(coordinate) - 1


def get_cpu_position() -> list:
    """Get random cpu position"""
    return [randint(0, 2), randint(0, 2)]


def check_for_winner() -> bool:
    """Check board if there is a winner"""
    if check_row(BOARD):
        return False
    if check_column(BOARD):
        return False
    if check_diagonal(BOARD):
        return False

    return True


def check_row(board) -> bool:
    """Checks board rows to determine winner"""
    for row in board:
        if row in WINNER:
            return True

    return False


def check_column(board) -> bool:
    """Retrieves column elements and checks if theres a winner"""
    columns = [[], [], []]  # type: list[list[int]]

    for row in board:
        columns[0].append(row[0])
        columns[1].append(row[1])
        columns[2].append(row[2])

    return check_row(columns)


def check_diagonal(board) -> bool:
    """Retrieves diagonal elements and checks if theres a winner"""
    diagonal = [[], []]  # type: list[list[int]]
    reversed_idx = 2

    for idx, row in enumerate(board):
        diagonal[0].append(row[idx])
        diagonal[1].append(row[reversed_idx])
        reversed_idx -= 1

    return check_row(diagonal)


def game_loop() -> None:

    while check_for_winner():
        display.update_display(ask_player_position(), "X")


game_loop()
