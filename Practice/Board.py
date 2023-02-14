## build a board class to represent the board of a standard board game
## the board is a 2D array of 0s

class Board:
    def __init__(self, rows, cols):
        pass

    def __str__(self):
        return "Hello"



def main():
    b = Board(8, 8)
    print(b) # should print a 8x8 board 
    """
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0
    """
main()