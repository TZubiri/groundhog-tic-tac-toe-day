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