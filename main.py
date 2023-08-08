from game import *

class Chess:
    
    def __init__(self) -> None:
        self.white = Player(1)
        self.black = Player(-1)
        
        self.board = self.white.get_board() + self.black.get_board()
    
    def move(self, color, x, y, new_x, new_y):
        if color == 1:
            result = self.white.move(self.board, x,y,new_x,new_y)
        else:
            result = self.black.move(self.board, x,y,new_x,new_y)
        
        if type(result) != bool:
            self.board = result
            return True
        
        # print('---Invalid Move---')
        return False


chess = Chess()
for c in [1, -1]*100:
    result = False
    while not result:
        # NOTE: c always stayes in '1'
        print(f'---{c} Turn---')
        print(chess.board)
        x = int(input('x   : '))
        y = int(input('y   : '))
        new_x = int(input('newx: '))
        new_y = int(input('newy: '))
        result = chess.move(c, x, y, new_x, new_y)
    