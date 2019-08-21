import random
import time


class TicTacToe(object):
    """
    O|1|O
    1|O|1
    O|1|O
    """
    def __init__(self, symbol):
        self.board = None
        self.init_board(symbol=symbol)
        self.xy_moves = [
            [0,0], [0,1], [0,2],
            [1,0], [1,1], [1,2],
            [2,0], [2,1], [2,2],
        ]

    def _get_xy(self):
        i = random.randint(0, len(self.xy_moves)-1)
        return self.xy_moves[i]

    def init_board(self, symbol="-"):
        self.board = []
        for _ in range(3):
            row = [symbol] * 3
            self.board.append(row)

    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    return False
        return True

    def make_move(self, symbol):
        if self.is_full():
            raise Exception("no legal move")

        i, j = self._get_xy()
        if self.board[i][j] == "-":
                self.board[i][j] = symbol
                return True
        return self.make_move(symbol)

    def add_token(self, x, y, symbol):
        if self.board[x][y] != "-":
            return False
        else:
            self.board[x][y] = symbol
            return True

    def print_board(self):
        print("\033[H\033[J")
        for i in range(3):
            print("|".join(self.board[i]))
        print(" ")

    def check_winner(self, symbol):
        s_win = symbol * 3
        for i in range(3):
            if s_win == "".join(self.board[i]) or s_win == "".join([self.board[j][i] for j in range(3)]):
                return True
        if s_win == "".join(self.board[i][i] for i in range(3)):
            return True
        if s_win == "".join(self.board[i][2-i] for i in range(3)):
            return True
        return False


ttt = TicTacToe("-")
ttt.print_board()

while True:
    if ttt.is_full():
        print("It's a tie")
        break
    # user placement
    s = raw_input("\"X\" move (ij), q to exit: ")
    if s == "q":
        break
    assert len(s) == 2, "can't parse indices"
    i = int(s[0])
    j = int(s[1])
    if ttt.add_token(i, j, "X"):
        ttt.print_board()
        if ttt.check_winner("X"):
            print("You won")
            break
        if not ttt.is_full():
            # machine placement
            print("\"O\" move")
            ttt.make_move("O")
            ttt.print_board()
            if ttt.check_winner("O"):
                print("You lost")
                break
    else:
        print("try again")
