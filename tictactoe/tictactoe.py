from random import randint
import time

class TicTacToe:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def print_instructions(self):
        print('Welcome to TicTacToe')
        print('Player 1 is X and Player 2 is O')
        print('Take turns placing your pieces - the first to 3 in a row wins!')
        return

    def print_board(self):
        print("  0 1 2")
        for i in range(len(self.board)):
            row = str(i) + " "
            for j in range(len(self.board[i])):
                row = row + str(self.board[i][j]) + " "
            print(row)
        return

    def is_valid_move(self, row, col):
        return "-" == self.board[row][col]

    def place_player(self, player, row, col):
        self.board[row][col] = player
        return

    def take_manual_turn(self, player):
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

    # return from the function if alpha greater than equal to beta
    def minimax_alpha_beta(self, player, depth, alpha, beta):
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
                        score = self.minimax_alpha_beta('X', depth - 1, alpha, beta)[0]
                        self.place_player('-', i, j)
                        if best < score:
                            opt_row = i
                            opt_col = j
                            best = score
                        alpha = max(alpha, best)
                        if alpha >= beta:
                            break
            return best, opt_row, opt_col

        if player == 'X':
            worst = 10
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.is_valid_move(i, j):
                        self.place_player(player, i, j)
                        score = self.minimax_alpha_beta('O', depth - 1, alpha, beta)[0]
                        self.place_player('-', i, j)
                        if worst > score:
                            opt_row = i
                            opt_col = j
                            worst = score
                        beta = min(beta, worst)
                        if beta <= alpha:
                            break
            return worst, opt_row, opt_col

    # currently using alpha beta minimax, can call minimax() for regular
    def take_minimax_turn(self, player, depth):
        start = time.time()
        score, row, col = self.minimax_alpha_beta(player, depth, -1000, 1000)
        end = time.time()
        print("This turn took:", end - start, "seconds")
        self.place_player(player, row, col)

    # NOTE: select depth > 0, else use take_random_turn()
    def take_turn(self, player):
        print(player + "'s Turn")
        if player == 'X':
            self.take_manual_turn(player)
        if player == 'O':
            depth = 4
            self.take_minimax_turn(player, depth)
        self.print_board()

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
        diags = [[self.board[0][0], self.board[1][1], self.board[2][2]],
                 [self.board[0][2], self.board[1][1], self.board[2][0]]]
        return [player, player, player] in diags

    def check_win(self, player):
        return self.check_row_win(player) or self.check_col_win(player) or self.check_diag_win(player)

    def check_tie(self):
        for i in range(len(self.board)):
            if '-' in self.board[i]:
                return False
        return not self.check_win('X') and not self.check_win('O')

    def play_game(self):
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
        if self.check_win('O'):
            print('Player 2 (O) Wins')
        if self.check_tie():
            print('Tie Game')