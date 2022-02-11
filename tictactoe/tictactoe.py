from random import randint

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def print_instructions(self):
        # TODO: Print the instructions to the game
        print('Welcome to TicTacToe')
        print('Player 1 is X and Player 2 is O')
        print('Take turns placing your pieces - the first to 3 in a row wins!')
        return

    def print_board(self):
        # TODO: Print the board
        print("  0 1 2")
        for i in range(len(self.board)):
            row = str(i) + " "
            for j in range(len(self.board[i])):
                row = row + str(self.board[i][j]) + " "
            print(row)
        return

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        return "-" == self.board[row][col]

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        row = input('Enter a row: ')
        col = input('Enter a column: ')
        while not self.is_valid_move(int(row), int(col)):
            print('Please enter a valid move')
            row = input('Enter a row: ')
            col = input('Enter a column: ')
        self.place_player(player, int(row), int(col))
        self.print_board()
        return

    def take_random_turn(self, player):
        rand_row = randint(0, 2)
        rand_col = randint(0, 2)
        while not self.is_valid_move(rand_row, rand_col):
            rand_row = randint(0, 2)
            rand_col = randint(0, 2)
        self.place_player(player, rand_row, rand_col)
        self.print_board()
        return

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + "'s Turn")
        if player == 'X':
            self.take_manual_turn(player)
        if player == 'O':
            self.take_random_turn(player)
        return

    # have to write all of the check win functions
    def check_col_win(self, player):
        for i in range(len(self.board)):
            col = []
            for j in range(len(self.board[i])):
                col.append(self.board[j][i])
            if [player, player, player] == col:
                return True
        return False

    def check_row_win(self, player):
        return [player, player, player] in self.board

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        diags = [[self.board[0][0], self.board[1][1], self.board[2][2]], [self.board[0][2], self.board[1][1], self.board[2][0]]]
        return [player, player, player] in diags

    def check_win(self, player):
        return self.check_row_win(player) or self.check_col_win(player) or self.check_diag_win(player)

    def check_tie(self):
        # TODO: Check tie
        for i in range(len(self.board)):
            if '-' in self.board[i]:
                return False
        return not self.check_win('X') and not self.check_win('O')

    def play_game(self):
        # TODO: Play game
        self.print_instructions()
        self.print_board()
        player = 'X'
        while not self.check_win('X') and not self.check_win('O') and not self.check_tie():
            self.take_turn(player)
            if 'X' in player:
                player = 'O'
            elif 'O' in player:
                player = 'X'

        if self.check_win('X'):
            print('Player 1 (X) Wins!')
            return
        if self.check_win('O'):
            print('Player 2 (O) Wins')
            return
        if self.check_tie():
            print('Tie Game')
            return

        return

