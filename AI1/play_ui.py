import AI1
import sys

if len(sys.argv) == 1:
	raise Exception("Please specify who plays X")

v = sys.argv[1]

def human_move(board):
	print(render_board(board))
	i = input('your move:')
	if len(i)==1:
		return AI1.make_move(board,int(i))
	elif len(i)==2:
		x,y = 0,0
		if i[0] in ("A","a"):
			x=1
		elif i[0] in ("B","b"):
			x=2
		elif i[0] in ("C","c"):
			x=3
		else:
			raise Exception("Didn't understand move (E2)")

		if i[1] in ("1","2","3"):
			y = int(i[1])
		else:
			raise Exception("Didn't understand move (E3)")

		i = i.lower()
		bytes(i,"ASCII")
		return AI1.make_move(board,(x-1)*3+y-1)
	else:
		raise Exception("Didn't understand move (E1)")
	return AI1.make_move(board,i)



if v == "1" or v =="default":
	AI = AI1.play_1
elif v == "2" or v=="bobo" or v=="random":
	AI = AI1.play_2
elif v == "0" or v=="none" or v=="" or v=="me" or v=="human":
	AI = human_move
else:
	raise Exception("unrecognized cli param")


def render_board(board):
	return board[:3] + '\n' + board[3:6] + '\n' + board[6:]

board = '_________'

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
