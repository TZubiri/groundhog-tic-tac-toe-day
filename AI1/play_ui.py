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
	AI = AI1.play_1 #first legal move left to right top down
elif v == "2" or v=="bobo" or v=="random":
	AI = AI1.play_2 #random
elif v == "3" or v=="1ply" or v=="1-ply":
	AI = AI1.play_3 #try to win
elif v == "4" or v=="1ply+" or v=="1-ply+":
	AI = AI1.play_4 #try to win, don't lose
elif v == "5" or v=="bruteforce" or v=="enumerateall":
	AI = AI1.play_5b
elif v == "0" or v=="none" or v=="" or v=="me" or v=="human":
	AI = human_move
else:
	raise Exception("unrecognized cli param")


def render_board(board):
	return board[:3] + '\n' + board[3:6] + '\n' + board[6:]

board = '_________'

p1 = human_move
p2 = AI

player = p1
while AI1.winner(board)=='':
	print("asd")
	board=player(board)
	player = p1 if player == p2 else p2



print(render_board(board))
print("winner is: "+ AI1.winner(board))
