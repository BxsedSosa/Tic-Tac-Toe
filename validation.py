"""All validation checks if input is good"""


def check_input_is_valid(user_input: str) -> bool:
    """Checks if the user input is within guidelines"""
    if (
        len(user_input) != 1
        or not user_input.isdigit()
        or int(user_input) not in range(1, 4)
    ):
        return True

    return False


def check_already_used_position(grid: list, coordinates: list) -> bool:
    """Check if the coordinates given is already used"""
    if grid[coordinates[0]][coordinates[1]] in ["x", "o"]:
        return True

    return False
