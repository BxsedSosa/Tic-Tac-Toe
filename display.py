"""Imports"""

from os import system
from time import sleep
from pyfiglet import Figlet

BORDER = "=" * 60
logo_font = Figlet(font="jazmine")
game_font = Figlet(font="banner")


def clear_console() -> None:
    """Clear console from text"""
    system("clear||cls")


def display_welcome_screen() -> None:
    """Displays welcome screen"""
    clear_console()
    print(logo_font.renderText("   Welcome"))
    print(logo_font.renderText("           to"))
    print(logo_font.renderText("tic tac toe"))
    sleep(3)


def display_try_again() -> None:
    """Displays try again"""
    clear_console()
    print(logo_font.renderText("Do you want to try again?"))
    print('Type in "yes" or "y" to play again')
    sleep(1)


def display_winner(player) -> None:
    """Displays winner"""
    clear_console()
    print(logo_font.renderText(f"{player} wins the game!"))
    sleep(2)


def display_end() -> None:
    """Displays end screen"""
    clear_console()
    print(logo_font.renderText("Thank you for playing"))
    sleep(1)


def display_tie() -> None:
    """Displays if there was a tie"""
    clear_console()
    print(logo_font.renderText("Its a tie!"))
    sleep(2)


def display_round_winner(player) -> None:
    """Displays round winner"""
    clear_console()
    print(logo_font.renderText(f"{player} wins the round!"))
    sleep(2)


def display_logo() -> None:
    """Displays tic tac toe logo"""
    print(BORDER)
    print(logo_font.renderText("Tic Tac Toe"))


def display_grid(grid) -> None:
    """Displays game grid"""
    for row in grid:
        print("  ".join(game_font.renderText(row)))


def display_score(player_score: int, cpu_score: int, game_round: int) -> None:
    """Displays score and rounds"""
    print(BORDER)
    print(
        f"Best of 3     Player : {player_score} | Cpu : {cpu_score}     Round: {game_round}\n".center(
            len(BORDER)
        )
    )


def display_game(grid, player_score=0, cpu_score=0, game_round=0) -> None:
    """Displays all combined displays needed"""
    clear_console()
    display_logo()
    display_grid(grid)
    display_score(player_score, cpu_score, game_round)
    sleep(1)
