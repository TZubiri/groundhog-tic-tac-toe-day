import AI1

def render_board(board):

    return board[:3] + '\n' + board[3:6] + '\n' + board[6:]

board = '_________'
print(render_board(board))

while AI1.winner(board)!='':

    o = int(input('O move:'))
    board = AI1.make_move(board,o)
    print(render_board(board))
    x = int(input('X move:'))
    board = AI1.make_move(board,x)
    print(render_board(board))

print("Winner is: "+ AI1.winner(board))
