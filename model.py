# Mancala
#   model.py
#
# Created by Chase Carnaroli

class Game():
    
    def __init__(self, avalanche_mode: bool = False, init_condit: [int] = None):
        self.avalanche = avalanche_mode

        # The players in the game are represented by numbers
    
        self.PLAYER_ONE = 1
        self.PLAYER_TWO = 2
        
        self.current_turn = self.PLAYER_TWO

        if init_condit != None:
            self.pits = init_condit
        else:
            # pits represents the number of marbles in each spot on the board
            #
            # By default, each pit starts with 4 pieces and the store starts with 0
            #
            #   0 - 5           PLAYER 1's PITS
            #   6               PLAYER 1's STORE
            #   7 - 12          PLAYER 2's PITS
            #   13              PLAYER 2's STORE
    
            self.pits = [4] * 6 + [0] + [4] * 6 + [0] 


    def switch_turn(self):
        'Switch the current turn to the other player'
        if self.current_turn == self.PLAYER_ONE:
            self.current_turn = self.PLAYER_TWO
        else:
            self.current_turn = self.PLAYER_ONE


    def get_winner(self) -> (str):
        'Determines winner and returns winner'
        if self.pits[6] > self.pits[13]:
            return self.PLAYER_ONE
        elif self.pits[6] < self.pits[13]:
            return self.PLAYER_TWO
        else:
            return 3


    def clear_remaining_pieces(self) -> [int]:
        'Clear remains pieces to the right store and return the pits'
        # First row
        for pit in range(0,6):
            if self.pits[pit] > 0:
                self.pits[6] += self.pits[pit]
                self.pits[pit] = 0

        # Second row
        for pit in range(7,13):
            if self.pits[pit] > 0:
                self.pits[13] += self.pits[pit]
                self.pits[pit] = 0

        return self.pits
    

    def check_game_over(self) -> bool:
        'Returns whether or not the game is over'
        p_one_pits = self.pits[0:6]
        p_two_pits = self.pits[7:13]

        player_one_pits_empty = self._check_empty(p_one_pits)
        player_two_pits_empty = self._check_empty(p_two_pits)

        return player_one_pits_empty or player_two_pits_empty
        

    def _check_empty(self, pits: [int]) -> bool:
        'Returns true if list is empty, false otherwise'
        # Checks each item in the list
        # If one is not 0, it returns False
        for pit in pits:
            if pit != 0:
                return False

        # If it made it through, then the list is empty
        return True
        
        


    def make_move(self, pit: int) -> (bool, int):
        'Returns true if move is over, false otherwise'
        ending_pos = self._move_pieces(pit)
        
        if ending_pos == 6 or ending_pos == 13:
            return (False, ending_pos)
        else:
            return (True, ending_pos)
        
            
    

    def check_valid_move(self, pit: int) -> bool:
        # Check to make sure chosen pit was valid
        # A move is invalid if:
        #   pit is outside of the range
        #   pit is a store (6 or 14)
        #   pit is on the opponents side
        #   pit is empty
        #
        if (((0 <= pit <= 5 and self.current_turn == self.PLAYER_ONE)
             or (7 <= pit <= 12 and self.current_turn == self.PLAYER_TWO))
            and (self.pits[pit] != 0)):
                return True
        else:
            return False

        

    def _move_pieces(self, pit: int) -> int:
        'Moves the pieces from the pit and returns the ending position'

        # Get number of pieces in the pit
        num_pieces = self.pits[pit]

        # Sets pit to 0, since the pieces are being taken out
        self.pits[pit] = 0

        # Loops until all the pieces have been placed
        while num_pieces > 0:
            pit += 1

            # Check to make sure pit does not go out of bounds
            if pit > 13:
                pit = 0

            # Check to make sure pit is not opponent's store
            if ((pit == 6 and self.current_turn == self.PLAYER_TWO) or
                (pit == 13 and self.current_turn == self.PLAYER_ONE)):
                    continue
            else:
                # Drop one of the pieces into that pit
                self.pits[pit] += 1
                num_pieces -= 1


        # Once loop is done, return the pit it ended on
        return pit
            

    def attempt_steal(self, pit: int) -> bool:
        'Sees if it can steal opponents pieces, returns result'
        # If there is only one in the pit, then it must have been empty before
        if pit == 6 or pit == 13:
            return False
        elif (self.current_turn == self.PLAYER_ONE and pit > 6) or (self.current_turn == self.PLAYER_TWO and pit < 6):
            return False
        elif self.pits[pit] == 1:
            return True
        else:
            return False
            
                    

    def steal(self, pit: int) -> None:
        'Steals the pieces from an opponents pit and puts them in own store'
        diff = 6 - pit
        pit_to_steal = 6 + diff

        if pit > 6:
            self.pits[13] += self.pits[pit_to_steal]
        elif pit < 6:
            self.pits[6] += self.pits[pit_to_steal]

        self.pits[pit_to_steal] = 0
            
