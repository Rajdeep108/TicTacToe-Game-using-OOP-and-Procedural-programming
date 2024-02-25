def greet(player1, player2):
    print('Let\'s play!!!')
    print('Player 1 is', player1)
    print('Player 2 is', player2)

def print_board(board):
    for row in board:
        print("|".join(row))
        print('-' * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '+':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '+':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '+':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '+':
        return board[0][2]

    return None

def play(player1, player2):
    greet(player1, player2)
    board = [['+' for _ in range(3)] for _ in range(3)]
    current_player = player1

    while True:
        print_board(board)
        print(f"Player {current_player}, choose your move (e.g., row column): ")
        move = input().strip().split()
        if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
            print("Invalid input! Please enter row and column numbers separated by space.")
            continue
        row, col = map(int, move)
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != '+':
            print("Invalid move! Try again.")
            continue
        board[row - 1][col - 1] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Congratulations! Player {winner} wins!")
            break
        elif all(all(cell != '+' for cell in row) for row in board):
            print_board(board)
            print("It's a draw!")
            break
        current_player = player2 if current_player == player1 else player1

# Example usage:
play('X', 'O')
