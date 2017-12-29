# Mancala
#   mancala.py
#
# Created by Chase Carnaroli
import gui
import model

def start_game() -> None:
    'Main code that runs the game'

    # Create UI
    ui = gui.Console_UI()

    # Deal with avalanche mode later

    # Create game
    game = model.Game()

    game_over = False

    while not game_over:
        # Switch turn
        game.switch_turns() 
        
        # Preform Move
        move_over = False
        while not move_over:
            # Get valid move
            while True:
                move = ui.get_move()
                if game.check_valid_move(move):
                    break

            move_status = game.make_move(move)
            move_over = move_status[0]
            ending_pos = move_status[1]

            ui.update(game.pits)

            # See if player stole opponent pieces
            steal_success = game.attempt_steal(ending_pos)

            if steal_success:
                ui.steal(ending_pos)
        
         # See if game is over
         game_over = game.check_game_over()

    print("Game Over")
        
        


if __name__ == '__main__':
    start_game()
