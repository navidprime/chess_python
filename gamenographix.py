from game import Chess

chess = Chess(print_=True)
for c in [1, -1]*100:
    result = False
    while not result:
        turn = 'White' if c == 1 else 'Black'
        print(f'---{turn} Turn---')
        print(chess.board)
        x = int(input('x   : '))
        y = int(input('y   : '))
        new_x = int(input('newx: '))
        new_y = int(input('newy: '))
        result = chess.move(c, x, y, new_x, new_y)