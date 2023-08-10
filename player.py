import numpy as np
from piece import *

class Player:
    
    def __init__(self, color, print_) -> None:
        assert color in (1, -1)
        
        self.color = color
        self.print_ = print_
        
        pawn_y = 1
        core_y = 0
        if color == 1:
            pawn_y = 6
            core_y = 7
        
        self.pieces = {
            'pawn': [Piece(x, pawn_y) for x in range(8)],
            'rook': [Piece(x, core_y) for x in (0, 7)],
            'knight': [Piece(x, core_y) for x in (1, 6)],
            'bishop': [Piece(x, core_y) for x in (2, 5)],
            'queen': [Piece(3, core_y)],
            'king': [Piece(4, core_y)],
        }
    
    def get_board(self):
        board = np.zeros((8,8), dtype=np.int32)
        
        for obj in NameMapping:
            for piece in self.pieces[obj.name.lower()]:
                board[piece.y, piece.x] = obj.value * self.color
        
        return board

    def move(self, board, x, y, new_x, new_y):
        
        # validate both x and y
        if not ((0 <= new_y < 8)\
            and (0 <= new_x < 8)):
            if self.print_:
                print('--*new_x and new_y are not valid')
            return False
        
        if not ((0 <= y < 8)\
            and (0 <= x < 8)):
            if self.print_:
                print('--*x and y are not valid')
            return False
        
        if board[y, x] == 0:
            if self.print_:
                print('--*can not select empty space for move')
        
        # move own piece
        if (board[y, x] <= 0 and self.color == 1)\
            or (board[y, x] >= 0 and self.color == -1):
                if self.print_:
                    turn = 'white' if self.color == 1 else 'black'
                    turn_ = 'black' if turn=='white' else 'white'
                    print(f'--*it is {turn} turn, but trying to move {turn_} pieces')
                return False
            
        if new_y == y and new_x == x:
            if self.print_:
                print('--*skiping move is not allowed')
            return False
        
        board = board.copy()
        
        # assert piece rule
        if not RuleMapping[abs(board[y, x])](self.color, board, x, y, new_x, new_y):
            if self.print_:
                print(f'--*piece({abs(board[y, x])}) can not make that move')
            return False
        
        # update board
        board[new_y, new_x] = board[y,x]
        board[y,x] = 0
        
        return board
        