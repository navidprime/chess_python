from enum import Enum

class NameMapping(Enum):
    pawn = 1
    knight = 2
    bishop = 3
    rook = 4
    queen = 5
    king = 6

class Piece:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def pawn_rule(color, board, x,y,newx,newy):
    return True
def knight_rule(color, board, x,y,newx,newy):
    return True
def bishop_rule(color, board, x,y,newx,newy):
    return True
def rook_rule(color, board, x,y,newx,newy):
    return True
def queen_rule(color, board, x,y,newx,newy):
    return True
def king_rule(color, board, x,y,newx,newy):
    return True

RuleMapping = [
    True,
    pawn_rule,
    knight_rule,
    bishop_rule,
    rook_rule,
    queen_rule,
    king_rule,
]