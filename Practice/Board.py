## build a board class to represent the board of a standard board game
## the board is a 2D array of 0s

from Cell import Cell
class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[Cell(i, j, 'B') for i in range(self.cols)] for j in range(self.rows)]


    def __str__(self):
        result = ""
        for i in range(self.rows):
            for j in range(self.cols):
                result += str(self.matrix[i][j]) + " "
            result += '\n'
        return result



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