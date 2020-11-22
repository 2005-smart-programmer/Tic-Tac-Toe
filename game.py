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
    print(board[0] + ' | ' + board[1] + ' | ' + board[2] + "     1 | 2 | 3") 
    print(board[3] + ' | ' + board[4] + ' | ' + board[5] + "     4 | 5 | 6")
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + "     7 | 8 | 9")

# In the following function that is the main we are calling all the other functions


def play_game():
    display_board()

    flip_turn()

    # Global variables are needed
    global game_still_going_on

    game_still_going_on = True
    
    while game_still_going_on:
        print('\n')
        # Global variables are needed
        global turn

        global input1
        global input2

        # If turn is equals to input1 then set it to input2, and if turn is equal to anything other than input1, then set it to input1
        if turn == input1:
            turn = input2

        else:
            turn = input1    
        
        # Now print whose turn is it
        print(turn + "'s turn")

        # Here are the three functions that we are calling here
        place_choice()
        
        check_for_winner()

        print('\n')
        flip_player()
# Next we have to place the choice of the two players into the board

def place_choice():
    # This choice is a input that says to enter a number from 1-9
    choice = input('Enter a number from 1-9: ')
     
    # Now we have to make sure that the input is updated

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

# Now we have to set the logic of how can one win in this tic-tac-toe game

# So now we define a function where we call two another functions

def check_for_winner():

    check_for_win()

    check_for_tie()

# This following function calls another three functions 

def check_for_win():

    check_for_rows()

    check_for_columns()

    check_for_diagonals()

# If there is no win, then there is surely a tie between the two players

# So now let's set the logic for that

def check_for_tie():

    # Global variables we need
    global game_still_going_on


    if '-' not in board:
        game_still_going_on = False

        # Global variables we need
        global player
        print('\n')
        print('It is a tie!')

    else:
        return   

    
# Now we have to check the rows, columns and the diagonals to know whether there is a win or there is a tie


def check_for_rows():
    global game_still_going_on

    row1 = board[0] == board[3] == board[6] != '-'
    row2 = board[1] == board[4] == board[7] != '-' 
    row3 = board[2] == board[5] == board[8] != '-' 

    if row1 or row2 or row3:
        game_still_going_on = False
        
    if row1:
        print('\n')
        print(board[0] + "'s win")
    elif row2: 
        print('\n')
        print(board[1] + "'s win")
    elif row3: 
        print('\n')
        print(board[2] + "'s win")


def check_for_columns():
    global game_still_going_on
    
    column1 = board[0] == board[1] == board[2] != '-'
    column2 = board[3] == board[4] == board[5] != '-' 
    column3 = board[6] == board[7] == board[8] != '-' 

    if column1 or column2 or column3:
        game_still_going_on = False
        
    if column1: 
        print('\n')
        print(board[0] + "'s win")
    elif column2: 
        print('\n')
        print(board[3] + "'s win")
    elif column3: 
        print('\n')
        print(board[6] + "'s win")


def check_for_diagonals():
    global game_still_going_on
    
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-' 
    

    if diagonal1 or diagonal2:
        game_still_going_on = False
        
    if diagonal1: 
        print('\n')
        print(board[0] + "'s win")
    elif diagonal2: 
        print('\n')
        print(board[2] + "'s win")

# Now we have to flip the turn of the players

def flip_turn():
    global turn

    global input1

    global input2

    
    input1 = input('The one playing with X is: ')
        
    print('\n')

    turn = input1

    input2 = input('The one playing with O is: ')

    if turn == input1:
        turn = input2

    else:
        turn = input1


# This function is same as the upper function

def flip_player():
    global player

    if player == 'X':
        player = '0'

    else:
        player = 'X'                         

# Now we have to start the execution of the tic-tac-toe game

play_game()


# So here is it --- My Tic-Tac-Toe game 
