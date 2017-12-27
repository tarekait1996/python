from IPython.display import clear_output

boardGame = ['_']*9

def display_board(board):
    print(boardGame[0], ' | ', boardGame[1], ' | ', boardGame[2])
    print(boardGame[3], ' | ', boardGame[4], ' | ', boardGame[5])
    print(boardGame[6], ' | ', boardGame[7], ' | ', boardGame[8])

def reset_board():
    global boardGame
    boardGame = ['_']*9

def full_board_check(board):
    return not '_' in board
def space_check(board, position):
    return '_' == board[position]
def replay():
    print('do you want to play again (y/n) ')
def place_marker(board, marker, position):
    board[position] = marker
def player_input(mark):
    global boardGame
    req = 'choose your position where you want to set ' + mark + ': '

    while True:
        try:
            position = int(input(req)) - 1

        except valueError:
            print ("please enter a valid number between 1-9 ")
            continue
        if space_check(boardGame,position):
            place_marker(boardGame, mark, position)
            break
        else:
            print('this position is already taken.')
            continue

def isWon(board, mark):
    return (board[0] == board[1] == board[2] == mark) or\
           (board[3] == board[4] == board[5] == mark) or \
           (board[6] == board[7] == board[8] == mark) or \
           (board[0] == board[3] == board[6] == mark) or \
           (board[1] == board[4] == board[7] == mark) or \
           (board[2] == board[5] == board[8] == mark) or \
            (board[0] == board[4] == board[8] == mark) or \
            (board[6] == board[4] == board[2] == mark)

print('hi lets play a game! ')

while True:

    while not (isWon(boardGame, 'X') or isWon(boardGame,'O')):
        player_input('X')
        player_input('O')
        display_board(boardGame)
    if isWon(boardGame, 'X'):
        print('Player 1 has won! Congratulation')
        answer = input('Would you want to play again? (y/n)')
        play_again = (answer == 'y' or answer == 'Y')

        if not play_again :
            break
        else :
            reset_board()
            print('\n')
            continue
