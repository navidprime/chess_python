from game import Chess
import numpy as np
import pygame

class Game:
    
    def __init__(self, bsize, fps, print_=True) -> None:
        self.bsize=bsize
        self.w = bsize*8
        self.h = bsize*8
        
        self.fps = fps

        self.images = [
        pygame.image.load('./media/pawn.png'),
        pygame.image.load('./media/knight.png'),
        pygame.image.load('./media/bishop.png'),
        pygame.image.load('./media/rook.png'),
        pygame.image.load('./media/queen.png'),
        pygame.image.load('./media/king.png'),
        
        pygame.image.load('./media/pawnb.png'),
        pygame.image.load('./media/knightb.png'),
        pygame.image.load('./media/bishopb.png'),
        pygame.image.load('./media/rookb.png'),
        pygame.image.load('./media/queenb.png'),
        pygame.image.load('./media/kingb.png'),
        ]
        
        self.images = [self.get_img_fixed(img) for img in self.images]
        
        self.colors = [
            '#321e10', # brown (board bg)
            '#c6a87a', # tane (board bg)
        ]
        
        self.border = self.get_img_fixed(pygame.image.load('./media/border.png'))
        self.border2 = self.get_img_fixed(pygame.image.load('./media/border2.png'))
        self.border3 = self.get_img_fixed(pygame.image.load('./media/border3.png'))
        
        self.chess = Chess(print_)
        
        pygame.init()

        self.screen = pygame.display.set_mode((self.w, self.h))

        self.clock = pygame.time.Clock()

        self.board_bg = np.tile(np.array([[0,1],[1,0]]), (4,4))

        self.selected_x = None
        self.selected_y = None
        self.selected_img = None
        
        self.turn = 1
        
    def get_img_fixed(self, img):
    
        img = pygame.transform.scale(img, (self.bsize, self.bsize))
        
        return img
    
    def draw_block(self, x, y, image, is_surface):
        if is_surface:
            t = pygame.surface.Surface((self.bsize, self.bsize))
            t.fill(image) # image is a color here
            self.screen.blit(t, (y*self.bsize, x*self.bsize))
        else:
            self.screen.blit(image, (y*self.bsize, x*self.bsize))
    
    def step(self):
        result = None
        chess_board = self.chess.board
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        # draw pieces and board
        for i in range(8):
            for j in range(8):
                c = self.colors[0] if self.board_bg[i,j] == 1 else self.colors[1]
                self.draw_block(i, j, c, True) # first draw background
                
                if chess_board[i, j] < 0:
                    img = self.images[abs(chess_board[i,j])-1+6]
                
                    self.draw_block(i, j, img, False)
                elif chess_board[i, j] > 0:
                    img = self.images[abs(chess_board[i,j])-1]
                
                    self.draw_block(i, j, img, False) # then piece
        
        x, y = pygame.mouse.get_pos()
        
        # draw the border around square
        self.draw_block(y//self.bsize, x//self.bsize, self.border, False)
        
        left_pressed, *_ = (pygame.mouse.get_pressed())

        # handle moving pieces
        if left_pressed:
            if self.selected_x == None and chess_board[int(y//self.bsize),int(x//self.bsize)] != 0:
                
                self.selected_x = x
                self.selected_y = y
                if chess_board[int(y//self.bsize),int(x//self.bsize)] < 0:
                    self.selected_img = self.images[abs(chess_board[int(y//self.bsize),int(x//self.bsize)])-1+6]
                else:
                    self.selected_img = self.images[abs(chess_board[int(y//self.bsize),int(x//self.bsize)])-1]
            else:
                if self.selected_img != None:
                    self.draw_block(int(y//self.bsize), int(x//self.bsize), self.selected_img, False)
            
            if self.selected_x != None:
                # draw a border that indicates the current moving piece
                self.draw_block(int(self.selected_y//self.bsize), int(self.selected_x//self.bsize), self.border2, False)
        else:
            
            if self.selected_x != None:
                result = self.chess.move(self.turn, int(self.selected_x//self.bsize) ,int(self.selected_y//self.bsize), int(x//self.bsize), int(y//self.bsize))
                if result:
                    self.turn *= -1
            
            self.selected_x = None
            self.selected_y = None
            self.selected_img = None

        # draw a border left top/down for indicating turn
        if self.turn == 1:
            self.draw_block(7, 0, self.border3, False)
        else:
            self.draw_block(0, 0, self.border3, False)
        
        self.clock.tick(self.fps)
        pygame.display.update()
        
        return result

game = Game(60, 30)

while True:
    # will return None if any move wasn't taken
    # else retuns True or False which indicate the move was made or not
    game.step()