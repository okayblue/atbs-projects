# chess

theBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
		'3e': 'wking'}
		
def isValidChessBoard(board):
	valid = ''
	
	# Checking for king and queen
	if 'bking' not in board.values() or 'wking' not in board.values():
		valid = False
	
	wpieces = 0
	bpieces = 0
	wpawns = 0
	bpawns = 0
	wkings = 0
	bkings = 0
	
	# Check for correct number of pieces
	for i in board:
		if board[i] == 'wking' or board[i] == 'wqueen' or board[i] == 'wbishop' or board[i] == 'wrook'or board[i] == 'wpawn': 
			wpieces += 1
		if board[i] == 'bking' or board[i] == 'bqueen' or board[i] == 'bbishop' or board[i] == 'brook'or board[i] == 'bpawn': 
			bpieces += 1
		if board[i] == 'wpawn':
			wpawns += 1
		if board[i] == 'bpawn':
			bpawns += 1
		if board[i] == 'wking':
			wkings += 1
		if board[i] == 'bking':
			bkings += 1
		if wpieces > 16 or bpieces > 16 or wpawns > 8 or bpawns > 8 or wkings > 1 or bkings > 1:
			valid = False
			break
		
		# Checking for valid spaces	
		for i in board:
			if i[1] not in 'abcdefgh':
				valid = False
				break
			
		for i in board:
			if i[0] not in '12345678':
				valid = False
				break
			
	if valid == False:
		print('This is not a valid chess board')
		return False
	else:
		print('This is a valid chess board')
		return True

