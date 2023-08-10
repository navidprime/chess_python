from player import *

class Chess:
    
    def __init__(self, print_:bool=True) -> None:
        self.white = Player(1, print_)
        self.black = Player(-1, print_)
        
        self.n_white_win = 0
        self.n_black_win = 0
        
        self.board = self.white.get_board() + self.black.get_board()
    
    def move(self, color, x, y, new_x, new_y):
        if color == 1:
            result = self.white.move(self.board, x,y,new_x,new_y)
        else:
            result = self.black.move(self.board, x,y,new_x,new_y)
        
        if type(result) != bool:
            self.board = result
            return True
        
        return False
    
    def reset_board(self):
        self.board = self.white.get_board() + self.black.get_board()

    def check_king(self):
        if not np.any(self.board == 6):
            self.n_black_win += 1
            return 1 # white kind died
        elif not np.any(self.board == -6):
            self.n_white_win += 1
            return -1 # black king died
        else:
            return 0