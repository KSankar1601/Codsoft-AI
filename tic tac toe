def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != '-' for row in board for cell in row)

def get_valid_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            x, y = divmod(move, 3)
            if 0 <= x < 3 and 0 <= y < 3 and board[x][y] == '-':
                return x, y
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-9).")

def main():
    board = [['-' for _ in range(3)] for _ in range(3)]
    player = 'X'

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not is_board_full(board):
        x, y = get_valid_move(board)
        board[x][y] = player
        print_board(board)
        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        player = 'O' if player == 'X' else 'X'
    else:
        print("It's a draw!")

if __name__ == '__main__':
    main()
