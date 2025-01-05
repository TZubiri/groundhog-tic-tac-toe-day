EMPTY_PIECE = '_'
PLAYER1_PIECE = 'o'
PLAYER2_PIECE = 'x'

def play_1(board):
    chosen_move = legal_moves(board)[0]
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

def make_move(board,square):
    # this is actually just board[square] = turn(board)
    board = board[:square] + turn(board) + board[square+1:]
    return board

def winner(board):
	lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
	for line in lines:
		if board[line[0]]!= '_' and board[line[0]] == board[line[1]] == board[line[2]]:
			return board[line[0]]
	return ''
	#return 'X'
	#return 'Y'
	#return ''
