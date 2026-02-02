# TIC TAC TOE (Python Progarm)

## Introduction
This is a simple command-line implementation of the Tic Tac Toe game in Python. The game allows you to play against the computer. The computer will make its moves based on some predefined rules to try and defeat you.

## How to Play
1. Run the script to start the game.
2. You will be prompted to choose between 'X' and 'O'.
3. After the selection, the board will be displayed, and the computer will perform a coin toss to decide who goes first.
4. If the user wins the coin toss, they will make the first move; otherwise, the computer will make the first move.
5. When it's the user's turn, they need to enter the row and column numbers (0, 1, or 2) to place their symbol ('X' or 'O') on the board.
6. The game will continue until one player wins, or the board is full (a tie game).

## Rules
- The game board is represented as a 3x3 grid.
- To win the game, a player must have their symbol ('X' or 'O') consecutively in a row, column, or diagonal.
- The computer will try to prevent the user from winning by placing its symbol ('X' or 'O') accordingly.
- If all the positions on the board are filled, and there is no winner, the game ends in a tie.

## Program Structure
The Tic Tac Toe game is structured as follows:

1. Import the required module for the coin toss.
2. Define functions for different aspects of the game:
   - `select_letter()`: Asks the user to select 'X' or 'O'.
   - `board()`: Initializes the game board.
   - `draw_board(board)`: Draws the game board with current positions.
   - `clean_board()`: Prepares a clean board for the game.
   - `is_board_full(board)`: Checks if the board is full (no empty positions left).
   - `insert_letter(board, letter, position)`: Inserts a letter (X or O) in a specific position on the board.
   - `is_winner(board, letter)`: Checks if a player has won the game.
   - `computer_moves(board, comp, letter)`: Handles the computer's moves based on predefined rules.
   - `repeat_game()`: Asks the user if they want to play again after the game ends.
   - `play_game()`: Handles the overall game flow and calls other functions accordingly.
   - `main()`: The entry point of the program that starts the game.

## Note

- Make sure to run the program using a Python interpreter.

## Contact
For further queries contact farwah.hamid21@gmail.com


