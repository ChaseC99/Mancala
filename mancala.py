# Mancala
#   mancala.py
#
# Created by Chase Carnaroli
import ui
import model

def start_game() -> None:
    'Main code that runs the game'

    # Create UI
    ui = ui.console_ui()

    # Deal with avalanche mode later

    # Create game
    game = model.Game()

    play = True

    while play:
        # Do game


if __name__ == '__main__':
    start_game()
