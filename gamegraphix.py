from game import Chess
import numpy as np
import pygame

BLOCK_SIZE = 60
W,H = BLOCK_SIZE*8, BLOCK_SIZE*8

colors = [
    '#5c2e12', # brown 1 (bg)
    '#321e10', # brown 2 (board bg)
    '#c6a87a', # tane (board bg)
]

images = [
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

border = pygame.image.load('./media/border.png')

chess = Chess(True)

pygame.init()

screen = pygame.display.set_mode((W, H))

screen.fill(colors[0])

clock = pygame.time.Clock()

board_bg = np.tile(np.array([[0,1],[1,0]]), (4,4))

def get_img_fixed(img):
    
    img = pygame.transform.scale(img, (BLOCK_SIZE, BLOCK_SIZE))
    
    return img

def draw_board():
    for i in range(8):
        for j in range(8):
            t = pygame.surface.Surface((BLOCK_SIZE, BLOCK_SIZE))
            c = colors[1] if board_bg[i,j] == 1 else colors[2]
            t.fill(c)
            screen.blit(t, (i*BLOCK_SIZE, j*BLOCK_SIZE))

def draw_pieces():
    for i in range(8):
        for j in range(8):
            if chess.board.T[i,j] != 0:
                if chess.board.T[i,j] < 0:
                    t = get_img_fixed(images[abs(chess.board.T[i,j])-1+6])
                else:
                    t = get_img_fixed(images[abs(chess.board.T[i,j])-1])
                screen.blit(t, (i*BLOCK_SIZE, j*BLOCK_SIZE))

def get_hovered_piece_cord(x, y):
    return (y//BLOCK_SIZE, x//BLOCK_SIZE)

def draw_border_on_piece(x, y):
    screen.blit(get_img_fixed(border), (y*BLOCK_SIZE, x*BLOCK_SIZE))

def get_image_transparented(img, alpha=.1):
    img = img.copy()
    img.fill((255, 255, 255, int(alpha*255)), None, pygame.BLEND_RGBA_MULT)
    return img

def draw_img(x, y, img):
    screen.blit(img, (y, x))

selected_img = None
selected_x = None
selected_y = None
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    x, y = get_hovered_piece_cord(*pygame.mouse.get_pos())
    
    draw_board()
    draw_pieces()
    draw_border_on_piece(x, y)
    
    left_pressed, center_pressed, right_pressed = (pygame.mouse.get_pressed())
    
    if left_pressed:
        if selected_img == None:
            if chess.board.T[y, x] < 0:
                selected_img = get_img_fixed(images[abs(chess.board.T[y,x])-1+6])
            elif chess.board.T[y, x] > 0:
                selected_img = get_img_fixed(images[abs(chess.board.T[y,x])-1])        
        else:
            # print(selected_x, selected_y, x, y)
            result = chess.move(1, selected_y, selected_x, y, x)
            if result:
                selected_x = None
                selected_y = None
                selected_img = None
            
        if selected_x == None:
            selected_x = x
            selected_y = y
            
    if selected_img != None:
        x, y = pygame.mouse.get_pos()
        
        draw_img(y, x, selected_img)
        t = pygame.surface.Surface((BLOCK_SIZE, BLOCK_SIZE))
        c = colors[1] if board_bg[selected_x, selected_y] == 1 else colors[2]
        t.fill(c)
        draw_img(selected_x*BLOCK_SIZE, selected_y*BLOCK_SIZE, t)
        draw_img(selected_x*BLOCK_SIZE, selected_y*BLOCK_SIZE, get_image_transparented(selected_img))
    
        
    if right_pressed:
        selected_img = None
        selected_x = None
        selected_y = None
            
    clock.tick(60)
    pygame.display.update()