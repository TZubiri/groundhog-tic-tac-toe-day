import AI1

def render_board(board):

    return board[:3] + '\n' + board[3:6] + '\n' + board[6:]

board = '_________'
print(render_board(board))

while True:
    i = int(input('your move:'))
    board = AI1.make_move(board,i)
    print(render_board(board))
    board = AI1.play_1(board)
    print('ai\'s move:')
    print(render_board(board))
