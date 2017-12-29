# Mancala
#   gui.py
#
# Created by Chase Carnaroli

class Console_UI():
    def get_move(self) -> int:
        try:
            return int(input('Enter pit: '))
        except:
            return self.get_move()


    def update(self, pits: [int]):
        'Prints the board'
        # Print first row
        print('  ', end='')
        print(pits[12], pits[11], pits[10], pits[9], pits[8], pits[7], sep=' ')

        # Print the stores, with a gap inbetween
        print(pits[13], ' ' * 11, pits[6])

        # Print second row
        print('  ', end='')
        for pit in pits[:6]:
            print(pit, end=' ')
