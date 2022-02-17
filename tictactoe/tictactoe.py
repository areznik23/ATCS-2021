from random import randint


# narrow down the cylinder all the way
# at a point as long as it is on a part of the cylinder that cancels
# conceptualize the functions fully
# take slow and understand each part of the problem
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

    def minimax(self, player, depth):
        # trying to limit the depth being searched, how to determine what the return values are
        # depth equaling to zero should determine what the base case is

        opt_row = -1
        opt_col = -1

        if self.check_win('O'):
            return 10, None, None
        if self.check_tie():
            return 0, None, None
        if self.check_win('X'):
            return -10, None, None
        if depth == 0:
            return 0, None, None

        if player == 'O':
            best = -10
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.is_valid_move(i, j):
                        self.place_player(player, i, j)
                        score = self.minimax('X', depth - 1)[0]
                        self.place_player('-', i, j)
                        if best <= score:
                            opt_row = i
                            opt_col = j
                            best = score
            return best, opt_row, opt_col

        if player == 'X':
            worst = 10
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.is_valid_move(i, j):
                        self.place_player(player, i, j)
                        score = self.minimax('O', depth - 1)[0]
                        self.place_player('-', i, j)
                        if worst >= score:
                            opt_row = i
                            opt_col = j
                            worst = score
            return worst, opt_row, opt_col

    def take_minimax_turn(self, player, depth):
        score, row, col = self.minimax(player, depth)
        self.place_player(player, row, col)

    # NOTE: select depth > 0, else use take_random_turn()
    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        print(player + "'s Turn")
        if player == 'X':
            self.take_manual_turn(player)
        if player == 'O':
            depth = 1
            self.take_minimax_turn(player, depth)
        self.print_board()

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
        diags = [[self.board[0][0], self.board[1][1], self.board[2][2]],
                 [self.board[0][2], self.board[1][1], self.board[2][0]]]
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
