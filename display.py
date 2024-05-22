from pyfiglet import Figlet

logo_font = Figlet(font="larry3d")
game_font = Figlet(font="big")
border = "=" * 75

map = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"],
]


def display_logo() -> None:
    """Display Tic Tac Toe Logo"""
    print(logo_font.renderText("Tic Tac Toe"))
    print(border)


def display_map(map) -> None:
    for row in map:
        print(" ".join(row).center(len(border), " "))


def update_display(coordinates, mark) -> None:
    """Display board continuously"""
    display_logo()
    map[coordinates[0]][coordinates[1]] = mark
    display_map(map)
