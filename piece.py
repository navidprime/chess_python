from enum import Enum
import numpy as np

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
    enemy_indexes = [(i)*color*-1 for i in range(1, 7)]
    if x != newx: # attack
        if color == 1:
            if abs(newx-x) == 1 and y-newy == 1:
                if board[newy, newx] in enemy_indexes:
                    return True
        else:
            if abs(newx-x) == 1 and newy-y == 1:
                if board[newy, newx] in enemy_indexes:
                    return True
        
        return False
    else: # move
        if color == 1:
            is_first_move = True if y == 6 else False
            
            if is_first_move and y-newy == 2 and board[newy ,newx] == 0 and board[newy+1, newx]== 0:
                return True
            elif y-newy == 1 and board[newx, newy] == 0:
                return True
        else:
            is_first_move = True if y == 1 else False

            if is_first_move and newy-y == 2 and board[newy, newx]==0 and board[newy-1, newx] ==0:
                return True
            elif newy-y == 1 and board[newy, newx] == 0:
                return True
    
        return False
        
def knight_rule(color, board, x,y,newx,newy):
    if not abs(x-newx) + abs(y-newy) == 3:
        return False

    friend_indexes = [(i)*color for i in range(1, 7)]
    
    if board[newy, newx] not in friend_indexes:
        return True
    
def bishop_rule(color, board, x,y,newx,newy):
    if x == newx or y == newy: 
        return False
    
    friend_indexes = [(i)*color for i in range(1, 7)]
    enemy_indexes = [(i)*color*-1 for i in range(1, 7)]
    
    x_sign = int((x-newx)/(abs(x-newx)))
    y_sign = int((y-newy)/(abs(y-newy)))
    
    # if y < 0 -> go up
    # if y > 0 -> go down
    # if x < 0 -> left
    # if x > 0 -> right
    
    # x-newx == y-newy
    for i in range(0, abs(x-newx), int((x-newx)/(abs(x-newx)))):
        if board[y+(i*y_sign), x+(i*x_sign)] == 0 or (y+(i*y_sign) == y and x+(i*x_sign) == x):
            continue
        if board[y+(i*y_sign), x+(i*x_sign)] in enemy_indexes and i != abs(x-newx)-1:
            return False
        if board[y+(i*y_sign), x+(i*x_sign)] in friend_indexes:
            return False
    
    return True
def rook_rule(color, board, x,y,newx,newy):
    if not ((x == newx and y != newy) or (y == newy and x != newx)):
        print('here')
        return False
    
    friend_indexes = [(i)*color for i in range(1, 7)]
    enemy_indexes = [(i)*color*-1 for i in range(1, 7)]
    
    is_x_move = True if (y == newy and x != newx) else False
    
    if is_x_move:
        is_move_left = True if x - newx > 0 else False
        
        if is_move_left:
            for i in range(newx, x+1):
                if board[y, i] in friend_indexes and i!=x:
                    return False
                if board[y, i] in enemy_indexes and i!=newx:
                    return False
        else:
            for i in range(x, newx+1):
                if board[y, i] in friend_indexes and i!=x:
                    return False
                if board[y, i] in enemy_indexes and i!=newx:
                    return False
        return True
    else:
        is_move_up = True if y - newy > 0 else False
        
        if is_move_up:
            for i in range(newy, y+1):
                if board[i, x] in friend_indexes and i!=y:
                    return False
                if board[i, x] in enemy_indexes and i!=newy:
                    return False
        else:
            for i in range(y, newy+1):
                if board[i, x] in friend_indexes and i!=y:
                    return False
                if board[i, x] in enemy_indexes and i!=newy:
                    return False
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