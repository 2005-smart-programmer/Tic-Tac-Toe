# We are gonna make a tic-tac-toe app using Python
# So let's do this

# First we need to make a board

board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

global player

player = 'X'

global winner

winner = 'X'


# Now we have to display this board

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def play_game():
    display_board()

    global game_still_going_on

    game_still_going_on = True
    
    while game_still_going_on:
        print('\n')

        global player

        if player == 'X' or player == '0':
            print(player + "'s turn")

        
        place_choice()
        
        

        check_for_winner()

        flip_player()
# Next we have to place the choice of the two players into the board

def place_choice():
    choice = input('Enter a number from 1-9: ')
    
        

     
    valid = False
    while not valid:
        while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            choice = input('Enter a number from 1-9: ')
    
        choice = int(choice) - 1
        if board[choice] == '-':
           valid = True
        else:
            print('You cannot go there. Go again')
                

    global player

    board[choice] = player

    
    
    display_board()


def check_for_winner():

    check_for_win()

    check_for_tie()


def check_for_win():

    check_for_rows()

    check_for_columns()

    check_for_diagonals()


def check_for_tie():
    global game_still_going_on

    if '-' not in board:
        game_still_going_on = False
        global player
        print('It is a tie')

    else:
        return   

    


def check_for_rows():
    global game_still_going_on

    row1 = board[0] == board[3] == board[6] != '-'
    row2 = board[1] == board[4] == board[7] != '-' 
    row3 = board[2] == board[5] == board[8] != '-' 

    if row1 or row2 or row3:
        game_still_going_on = False
        
    if row1:
        print(board[0] + "'s win")
    elif row2:
        print(board[1] + "'s win")
    elif row3:
        print(board[2] + "'s win")


def check_for_columns():
    global game_still_going_on
    
    column1 = board[0] == board[1] == board[2] != '-'
    column2 = board[3] == board[4] == board[5] != '-' 
    column3 = board[6] == board[7] == board[8] != '-' 

    if column1 or column2 or column3:
        game_still_going_on = False
        
    if column1:
        print(board[0] + "'s win")
    elif column2:
        print(board[3] + "'s win")
    elif column3:
        print(board[6] + "'s win")


def check_for_diagonals():
    global game_still_going_on
    
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-' 
    

    if diagonal1 or diagonal2:
        game_still_going_on = False
        
    if diagonal1:
        print(board[0] + "'s win")
    elif diagonal2:
        print(board[2] + "'s win")


def flip_player():
    global player

    if player == 'X':
        player = '0'

    else:
        player = 'X'                         

play_game()


# So here is it --- My Tic-Tac-Toe game 
