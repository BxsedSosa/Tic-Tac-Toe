"""Imports"""

from math import cos
from random import randint
from display import game_board

PICKS = ["x", "o"]
WINNER = [[pick] * 3 for pick in PICKS]

game_board[0][0] = "x"
game_board[1][0] = "x"
game_board[2][0] = "x"

print("game", game_board)


def check_for_winner():

    def check_row(grid: list) -> str:
        for row in grid:
            if row in WINNER:
                return row[0]

        return ""

    def check_column(grid: list) -> str:
        column = []

        for index1 in range(len(grid)):
            column.append([grid[index2][index1] for index2 in range(len(grid))])

        return check_row(column)

    def check_diagonal(grid: list) -> str:
        diagonal = []

        diagonal.append(grid[row][idx] for idx, row in enumerate(grid))
        diagonal.append(grid[row][2 - idx] for idx, row in enumerate(grid))

        print(diagonal)

        return check_row(diagonal)

    print(check_row(game_board))
    print(check_column(game_board))
    print(check_diagonal(game_board))


check_for_winner()
