import AI1
import sys

v = sys.argv[1]

if v == "1" or v =="default":
    AI = AI1.play_1
elif v == "2" or v=="bobo" or v=="random":
    AI = AI1.play_2
elif v == "0" or v=="none" or v=="" or v=="me" or v=="human":
    AI = None
else:
    raise Exception("unrecognized cli param")


def render_board(board):
    return board[:3] + '\n' + board[3:6] + '\n' + board[6:]

board = '_________'

def human_move(board):
    print(render_board(board))
    i = int(input('your move:'))
    return AI1.make_move(board,i)

p1 = human_move
p2 = AI

turn = "O"
while AI1.winner(board)=='':
    if turn =="O":
        print("p1 turn")
        board=p1(board)
    elif turn =="X":
        board= p2(board)
    turn = "O" if turn == "X" else "X"



print(render_board(board))
print("winner is: "+ AI1.winner(board))
