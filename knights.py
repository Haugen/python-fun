def cannot_capture(board):
	for i,row in enumerate(board):
		for y,square in enumerate(row):
			if square == 1:
				if i < 6 and y > 1:
					if board[i+1][y-2] == 1 or board[i+2][y-1] == 1: return False
				if i < 6 and y < 6:
					if board[i+2][y+1] == 1 or board[i+1][y+2] == 1: return False
				if i > 1 and y > 1:
					if board[i-1][y-2] == 1 or board[i-2][y-1] == 1: return False
				if i > 1 and y < 6:
					if board[i-2][y+1] == 1 or board[i-1][y+2] == 1: return False
	return True

cannot_capture([
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 0]
]) # True

cannot_capture([
  [1, 0, 1, 0, 1, 0, 1, 0],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 1, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 0, 0, 1, 0, 1],
  [1, 0, 0, 0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0, 1, 0, 1]
]) # False