def print_board(board):
    """Prints the current state of the game board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_win(board):
    """Checks if there is a winner on the board."""
    
    win_conditions = [ [3, 4, 5], [6, 7, 8], ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return board[condition[0]]  # Returns 'X' or 'O'
    return None


def check_draw(board):
    """Checks if the board is full, resulting in a draw."""
    return " " not in board


def play_game():
    """Main game loop."""
   
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered 1 through 9 like this:")
    print(" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 ")
    
    while True:
        print_board(board)
        
       
        try:
            choice = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if choice < 0 or choice > 8:
                print("Invalid input. Please choose a number between 1 and 9.")
                continue
            if board[choice] != " ":
                print("That position is already taken! Choose another.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
            
        
        board[choice] = current_player
        
        
        winner = check_win(board)
        if winner:
            print_board(board)
            print(f"🎉 Congratulations! Player {winner} wins! 🎉")
            break
            
        if check_draw(board):
            print_board(board)
            print("🤝 It's a draw! Well played.")
            break
            
        
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
