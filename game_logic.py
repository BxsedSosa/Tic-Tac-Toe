"""All logic dealing with winning or tie"""

WINNER = [[pick] * 3 for pick in ["x", "o"]]


def check_for_winner(grid: list) -> bool:
    """Checks each way a player can win"""

    def check_row(grid: list) -> str:
        """Check if the row has 3 in a row"""
        for row in grid:
            if row in WINNER:
                return row[0]

        return ""

    def check_column(grid: list) -> str:
        """Check if the column has 3 in a row"""
        column = []

        for index1 in range(len(grid)):
            column.append([grid[index2][index1] for index2 in range(len(grid))])

        return check_row(column)

    def check_diagonal(grid: list) -> str:
        """Check if the diagonal row has 3 in a row"""
        diagonal = []

        diagonal.append([row[idx] for idx, row in enumerate(grid)])
        diagonal.append([row[2 - idx] for idx, row in enumerate(grid)])

        return check_row(diagonal)

    if check_row(grid):
        return True
    if check_column(grid):
        return True
    if check_diagonal(grid):
        return True

    return False


def check_for_tie(moves: int) -> bool:
    """If moves are maxed out and check_for_winner didnt trigger we get a tie"""
    if moves == 9:
        return True

    return False
