class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for row in [self.board[i:i + 3] for i in range(0, 9, 3)]:
            print(' | '.join(row))
            print('-' * 9)

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Position already occupied!")

    def is_winner(self, player):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board

    def is_game_over(self):
        return self.is_winner('X') or self.is_winner('O') or self.is_board_full()

    def play_game(self):
        while not self.is_game_over():
            self.print_board()
            try:
                position = int(input(f"Player {self.current_player}, enter your move (0-8): "))
                if position < 0 or position > 8:
                    print("Invalid input. Position must be between 0 and 8.")
                    continue
                self.make_move(position)
            except ValueError:
                print("Invalid input. Please enter a number.")
        self.print_board()
        if self.is_winner('X'):
            print("Player X wins!")
        elif self.is_winner('O'):
            print("Player O wins!")
        else:
            print("It's a draw!")

if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
