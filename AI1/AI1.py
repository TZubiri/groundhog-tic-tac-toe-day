EMPTY_PIECE = '_'
PLAYER1_PIECE = 'o'
PLAYER2_PIECE = 'x'

def play_1(board):
	chosen_move = legal_moves(board)[0]
	board_after_move = make_move(board,chosen_move)
	return board_after_move

import random
def play_2(board):
	moves = legal_moves(board)
	chosen_move = moves[random.randrange(len(moves))]
	board_after_move = make_move(board,chosen_move)
	return board_after_move


def legal_moves(board):
	legal_moves = []
	for i,square in enumerate(board):
		if square == EMPTY_PIECE:
			legal_moves.append(i)
	return legal_moves

def turn(board):
	# o is defined as the first to play
	os = board.count(PLAYER1_PIECE)
	xs = board.count(PLAYER2_PIECE)

	if os == xs:
		return PLAYER1_PIECE
	elif os == xs+1:
		return PLAYER2_PIECE
	else:
		raise Exception("Ilegal board state")

def make_move(board,square,piece = None):
	if piece== None:
		piece= turn(board)
	# this is actually just board[square] = turn(board)
	board = board[:square] + piece + board[square+1:]
	return board

def winner(board):
	lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
	for line in lines:
		if board[line[0]]!= '_' and board[line[0]] == board[line[1]] == board[line[2]]:
			return board[line[0]]
	if tie(board):
		return 'tie'
	return ''
	#return 'X'
	#return 'O'
	#return ''

def play_3(board):
	moves = legal_moves(board)
	for move in moves:
		if winner(newboard:=make_move(board,move)):
			return newboard
	return play_2(board)

def play_4(board):
	moves = legal_moves(board)
	turn_piece = turn(board)
	other_turn_piece = "o" if turn_piece == "x" else "x"
	print("piece, other turn piece",turn_piece,other_turn_piece)
	for move in moves:
		if winner(newboard:=make_move(board,move,turn_piece)):
			return newboard
	print("no winning move found")
	for move in moves:
		if winner(make_move(board,move,other_turn_piece)):
			return make_move(board,move,turn_piece)
	print("no immediate risk found")
	return play_2(board)


def tie(board):
	if board.count("_") == 0:
		return True
	else:
		return False
	#return True if board.count(board) == 0 else False

def play_5(board):
	ties = [] # would rather define this in-loop, can do for single var, but not for lists I don't think
	their_ties = []
	for move in legal_moves(board):
		newboard=make_move(board,move)
		if winner(newboard:=make_move(board,move)): #if we can win the game
			return newboard #win it
		elif tie(newboard): #if we can tie it
			ties.append(newboard) #save option for later
		else:	#else if the game is still undefined
			board3 = play_5(newboard)  #assume opponent would play like us.
			if winner(board3): #if opponent can win
				continue # discard our move
			elif tie(board3): #if opponent can tie
				their_ties.append(newboard) #save this move for later under the ones they can tie, 
							  #this distinction is valuable since we may prioritize situations
							  #where we force a tie if opponent can force our loss
							  #otherwise if they can tie a game, but they can also blunder, we would rather not take the early tie.
				continue  #continue search anyways
			else:
				return newboard  #if we can't force a win or a tie, and neither can opponent
	if ties:
		return ties[0] #if no ties, admit defeat.
	else:
		raise Exception ("I forfeit")

def play_5b(board): #->gamestate
	moves = legal_moves(board) #at the end of the day, we want to chose one of these
	for move in moves:
		if winner(newboard:=make_move(board,move)) or tie(newboard): #if we can win the game or tie it
			return newboard #do it
	goodmoves = []
	for move in moves:
		newboard = make_move(board,move)
		board3= play_5b(newboard)
		if board3 is None:
			return make_move(board,move)
		if winner(board3):
			continue
		goodmoves.append(move)
	if len(goodmoves) ==0:
		return None # Reduce good moves until zero or one, if more, choose 1 at random.
	return make_move(board,goodmoves[0])


#2ply then random
#specs:
#without using recursion or a main loop
#evaluate whether we win or opponent can win in the current turn, the next (opponet's turn),
#as well as our next turn and our opponent's next next turn.
#for these purposes one play is a pair of turns
def play_6(board0):
	possible_moves =[]
	moves1 = legal_moves(board0)
	for move1 in moves1:
		board1 = make_move(board0,move1)
		if winner(board1):
			return board1
		for move2 in legal_moves(board1):
			board2= make_move(board1,move2)
			if winner(board2):
				opponent_wins =True
				break
			for move3 in legal_moves(board2):
				board3= make_move(board2,move3)
				if winner(board3):
					player_wins =True
					break
			if locals().get("player_wins") ==True:
				player_wins == False
				continue
		if locals().get("opponent_wins") == True:
			opponent_wins = False
			continue
		else:
			pass
	return play_2(board)
#got to 3 half turns.
