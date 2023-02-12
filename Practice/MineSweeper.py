"""
mine_swipper

## Space - Board (higth, width), Square(symbol)
# Square = [value = {0-8,B}, is_hidden = {True, False}]
## rules - game logic:
# 1. תבחר משבצת מהלוח 
# 2. אם היא פצצה הפסדת 
# 3. תחשוף את המספר שעל המשבצת
# 4. אם הוא 0 אז לפתוח גם את השכנים 

"""

def is_valid_size(height, width):
    """ limit board and return an True if h, w are valid"""
    if not height.isdigit() or not width.isdigit():
        return False
    
    x, y = int(height), int(width)
    pass






def get_board_size():
    """get user to give you a number for height and width, validate and return it"""
    while True:
        height = input("please enter number of rows")
        width = input("please enter number of colums")
        if is_valid_size(height, width):
            return tuple(int(height), int(width))


def get_bomb_number():
    """get user to give you a number for bombs, validate and return it"""
    pass

def create_board(height, width):
    """nested list with height innter lists with width elements """
    pass

def get_user_choise():
    """get input from user validate it and return it"""
    pass

def place_choise(board, user_choise):
    """reveal the element in board that user choose"""
    pass

def is_game_over(board):
    """if a bomd is revealed return true"""
    pass

def is_win(board):
    """if the only unflipped sqares are bombs them you win"""
    pass

def print_board(board):
    pass


def populate(board, bomb_number):
    """randomly distribute bombs and numbers in the board"""
    pass

def main():
    # initialize
    height, width = get_board_size()
    bomb_number = get_bomb_number()
    board = create_board(height, width)
    populate(board, bomb_number)

    #Game logic
    while True:
        
        user_choise = get_user_choise()
        place_choise(board, user_choise)


        if is_game_over(board):
            print("You Lose")
            break

        if is_win(board):
            print("You win")
            break

        print_board(board)
