import random

class TicTacToeSinglePlayer:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.computer_player = 'O'

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

    def computer_move(self):
        available_moves = [i for i, val in enumerate(self.board) if val == ' ']
        if available_moves:
            position = random.choice(available_moves)
            self.make_move(position)

    def play_game(self):
        while not self.is_game_over():
            self.print_board()
            if self.current_player == 'X':
                try:
                    position = int(input("Your move (0-8): "))
                    if position < 0 or position > 8 or self.board[position] != ' ':
                        print("Invalid input. Please choose an empty cell between 0 and 8.")
                        continue
                    self.make_move(position)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Computer's move:")
                self.computer_move()
        self.print_board()
        if self.is_winner('X'):
            print("You win!")
        elif self.is_winner('O'):
            print("Computer wins!")
        else:
            print("It's a draw!")

if __name__ == '__main__':
    game = TicTacToeSinglePlayer()
    game.play_game()
