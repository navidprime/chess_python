from game import Chess

chess = Chess(print_=True)
for c in [1, -1]*100:
    king_died = chess.check_king()
    if king_died != 0:
        if king_died == 1:
            print('--white lose--')
        else:
            print('---black lose---')
        
        chess.reset_board()
        continue
        
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