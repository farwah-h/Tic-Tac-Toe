#Greetings
print ("-*-*-*-*-* TIC TAC TOE *-*-*-*-*-")
print ("*-*-*-*-*-*- WELCOME -*-*-*-*-*-*")

#Toss
import cointoss

#Selecting 'x' or 'o'
def select_letter():
    letter=" "
    comp=" "

    #ask letter to select a letter (X or O)
    while(letter != "x" and letter != "o"):
        letter=input("Select X or O: ")
        if letter == "x":
            letter = "x"
            comp = "o"
        elif letter == "o":
            letter = "o"
            comp = "x"
        else:
            print("Invalid")
        return letter,comp

#Board
def board():
    board = [
        [ " " , " " , " " ],
        [ " " , " " , " " ],
        [ " " , " " , " " ]
        ]
def draw_board(board):
    print(board[1],"  | ",board[2]," | ",board[3])
    print("----+-----+----")
    print(board[4],"  | ",board[5]," | ",board[6])
    print("----+-----+----")
    print(board[7],"  | ",board[8]," | ",board[9])
    return board

#to prepare a clean board for the game
def clean_board():
    #an empty board for X and O values
    board=[" " for x in range(10)]
    return board

#to check if board is full
def is_board_full(board):
    return board.count(" ")==0

#to insert a letter (X or O) in a specific position
def insert_letter(board,letter,position):
    board[position]=letter

#To Determine the Winner
def is_winner(board,letter):
        #Rows
    if board[1] == board[2] == board[3] and board[1] != " ":
        return True
    elif board[4] == board[5] == board[6] and board[4] != " ":
        return True
    elif board[7] == board[8] == board[9] and board[7] != " ":
        return True
        # Columns
    elif board[1] == board[4] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        return True
    elif board[3] == board[6] == board[9] and board[3] != " ":
        return True
        # Diagonals
    elif board[1] == board[5] == board[9] and board[1] != " ":
        return True
    elif board[3] == board[5] == board[7] and board[1] != " ":
        return True
    
#Computer Moves
def computer_moves(board,comp, letter):
        #All Possible Moves along the Rows
    if board[2] == board[3] == comp and board[1] == " ":
        board[1] = comp
    elif board[1] == board[2] == comp and board[3] == " ":
        board[3] = comp
    elif board[1] == board[3] == comp and board[2] == " ":
        board[2] = comp
    elif board[5] == board[6] == comp and board[4] == " ":
        board[4] = comp
    elif board[4] == board[6] == comp and board[5] == " ":
        board[5] = comp
    elif board[4] == board[5] == comp and board[6] == " ":
        board[6] = comp
    elif board[8] == board[9] == comp and board[7] == " ":
        board[7] = comp
    elif board[7] == board[9] == comp and board[8] == " ":
        board[8] = comp
    elif board[7] == board[8] == comp and board[9] == " ":
        board[9] = comp
        
        #All Possible Moves along the Columns
    elif board[1] == board[4] == comp and board[7] == " ":
        board[7] = comp
    elif board[1] == board[7] == comp and board[4] == " ":
        board[4] = comp
    elif board[4] == board[7] == comp and board[1] == " ":
        board[1] = comp
    elif board[2] == board[5] == comp and board[8] == " ":
        board[8] = comp
    elif board[2] == board[8] == comp and board[5] == " ":
        board[5] = comp
    elif board[5] == board[8] == comp and board[2] == " ":
        board[2] = comp
    elif board[3] == board[6] == comp and board[9] == " ":
        board[9] = comp
    elif board[3] == board[9] == comp and board[6] == " ":
        board[6] = comp
    elif board[6] == board[9] == comp and board[3] == " ":
        board[3] = comp
        
        #All Moves Along the Diagonals
    elif board[1] == board[5] == comp and board[9] == " ":
        board[9] = comp
    elif board[1] == board[9] == comp and board[5] == " ":
        board[5] = comp
    elif board[5] == board[9] == comp and board[1] == " ":
        board[1] = comp
    elif board[3] == board[5] == comp and board[7] == " ":
        board[7] = comp
    elif board[3] == board[7] == comp and board[5] == " ":
        board[5] = comp
    elif board[5] == board[7] == comp and board[3] == " ":
        board[3] = comp
        
        #Counter Moves at the Rows
    elif board[2] == board[3] == letter and board[1] == " ":
        board[1] = comp
    elif board[1] == board[3] == letter and board[2] == " ":
        board[2] = comp
    elif board[1] == board[2] == letter and board[3] == " ":
        board[3] = comp
    elif board[5] == board[6] == letter and board[4] == " ":
        board[4] = comp
    elif board[4] == board[6] == letter and board[5] == " ":
        board[5] = comp
    elif board[4] == board[5] == letter and board[6] == " ":
        board[6] = comp
    elif board[8] == board[9] == letter and board[7] == " ":
        board[7] = comp
    elif board[7] == board[9] == letter and board[8] == " ":
        board[8] = comp
    elif board[7] == board[8] == letter and board[9] == " ":
        board[9] = comp
        
        #Counter Moves along the Columns
    elif board[1] == board[4] == letter and board[7] == " ":
        board[7] = comp
    elif board[1] == board[7] == letter and board[4] == " ":
        board[4] = comp
    elif board[4] == board[7] == letter and board[1] == " ":
        board[1] = comp
    elif board[2] == board[5] == letter and board[8] == " ":
        board[8] = comp
    elif board[2] == board[8] == letter and board[5] == " ":
        board[5] = comp
    elif board[5] == board[8] == letter and board[2] == " ":
        board[2] = comp
    elif board[3] == board[6] == letter and board[9] == " ":
        board[9] = comp
    elif board[3] == board[9] == letter and board[6] == " ":
        board[6] = comp
    elif board[6] == board[9] == letter and board[3] == " ":
        board[3] = comp
        
        #Counter Moves Along the Diagonals
    elif board[1] == board[5] == letter and board[9] == " ":
        board[9] = comp
    elif board[1] == board[9] == letter and board[5] == " ":
        board[5] = comp
    elif board[5] == board[9] == letter and board[1] == " ":
        board[1] = comp
    elif board[3] == board[5] == letter and board[7] == " ":
        board[7] = comp
    elif board[3] == board[7] == letter and board[5] == " ":
        board[5] = comp
    elif board[5] == board[7] == letter and board[3] == " ":
        board[3] = comp
    
        #Special Case at the center
    elif board[5] == " ":
        board[5]=comp
        
        #Special Cases
    elif board[6] == letter and board[9] == " ":
        board[9] = comp
    elif board[4] == letter and board[8] == " ":
        board[8] = comp
    elif board[1] and board[9] == letter and board[2] == " ":
        board[2] = comp
    elif board[3] and board[7] and letter and board[2] and " ":
        board[2] = comp
    
        #Random 1st Moves
    elif board[9] == " ":
        board[9] = comp
    elif board[1] == " ":
        board[1] = comp
    elif board[3] == " ":
        board[3] = comp
    elif board[7] == " ":
        board[7] = comp
    elif board[2] == " ":
        board[2] = comp
    elif board[4] == " ":
        board[4] = comp
    elif board[8] == " ":
        board[8] = comp
    elif board[6] == " ":
        board[6] = comp
    
    
#to repeat the game
def repeat_game():

    repeat=input("Play again? Press y for yes and n for no: ")
    while repeat != "n" and repeat != "y":
        repeat=input("PLEASE, press y for yes and n for no: ")
    return repeat

#to play the game
def play_game():

    letter, comp= select_letter()
    #clean the board
    board=clean_board()
    board=draw_board(board)
    res = cointoss.toss()
    if res == False:  # human lost the toss
        # computer move
        computer_moves(board, comp, letter)
        # draw the board
        board = draw_board(board)
    #check if there are empty positions on the board
    while is_board_full(board) == False:
        
#Asking the User to input the row number and column number
        inarr = input("Enter row and column numbers to fix spot: ").split(" ")
        row,col = int(inarr[0]),int(inarr[1])
        print()
        
        if row==0:
            if col==0:
                position=1
            elif col==1:
                position=2
            elif col==2:
                position=3
        elif row==1:
            if col==0:
                position=4
            elif col==1:
                position=5
            elif col==2:
                position=6
        elif row==2:
            if col==0:
                position=7
            elif col==1:
                position=8
            elif col==2:
                position=9

        #check if user selects an occupied position by X or O
        if board[position] != " ":
            position=int(input("Please, choose an empty position to place an "+letter+ ":"))
#put the letter in the selected position & computer plays then draw the board
        insert_letter(board,letter,position)
        #computer move
        computer_moves(board,comp,letter)
        #draw the board
        board=draw_board(board)
       
        xx,oo = 0,0
        for v in board:
            if v == 'x':
                xx = xx + 1
            if v == 'o':
                oo = oo + 1
        sum = xx + oo
        if is_winner(board,letter):
            print("Congratulations! You Won.")
            return repeat_game()
        elif is_winner(board,comp):
            print("Hard Luck! Computer won")
            return repeat_game()
        elif sum == 9:
            print("Game Tie")
            return repeat_game()
    
    #if " " not in board:
    if is_board_full(board) == True:
        print("Tie Game :)")
        return repeat_game()

#Start the game
print("Welcome to Tic Tac Toe.")
repeat="y"
while(repeat=="y"):
    repeat=play_game()

