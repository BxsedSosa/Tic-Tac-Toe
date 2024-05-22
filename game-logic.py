from random import randint
import display

PICKS = ["X", "O"]
WINNER = [[pick] * 3 for pick in PICKS]


def ask_player_position() -> list:
    """Ask user for position they want to place mark"""
    x_coordinate = check_input(input("Please enter a row you want to mark:\n"))
    y_coordinate = check_input(input("Please enter a column you want to mark:\n"))
    coordinates = [x_coordinate, y_coordinate]

    return coordinates


def check_input(coordinate: str) -> int:
    """Checks if input is valid from user"""
    while len(coordinate) != 1 and not coordinate.isdigit():
        coordinate = input("Please only enter a number inbetween 1 to 3\n")

    return int(coordinate) - 1


def get_cpu_position() -> list:
    """Get random cpu position"""
    return [randint(0, 2), randint(0, 2)]


def check_for_winner() -> bool:
    """Check board if thers a winner"""
    board = display.map

    check_row(board)

    return False


def check_row(board) -> bool:
    """Checks board rows to determine winner"""
    for row in board:
        if row in WINNER:
            return True

    return False


def game_loop() -> None:
    display.update_display(ask_player_position(), "X")


print(ask_player_position())
# game_loop()
