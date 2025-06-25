def checkmate(board):
    try:
        rows = board.strip().split("\n")
        if not rows:
            print("Fail")
            return
        board = []
        for r in rows:
            board.append(list(r))
        if len(board) == 0:
            print("Fail")
            return
        
        num_rows = len(board)
        num_column = len(board[0])

        if num_rows > 8 or num_rows < 1 or num_column > 8 or num_column < 1:
            print("Fail")
            return

        if num_rows != num_column:
            print("Fail")
            return
        
        for row in board:
            if len(row) != num_column:
                print("Fail")
                return

        king_count = 0
        king_row , king_col = 0 , 0

        for i in range(num_rows):
            for j in range(num_column):
                if board[i][j] not in "KPQRB.":
                    print("Fail")
                    return
                elif board[i][j] == "K":
                    king_count += 1
                    king_row , king_col = i , j
        
        if king_count != 1:
            print("Fail")
            return
  
        if king_checkmate(board, king_row, king_col, num_rows, num_column):
            print("Checkmate")
        else:
            print("Not checkmate")
            return
        
    except:
        print("Fail")
        return
    
def check(board, king_row, king_col, row):

    for i in range(row):
        for j in range(row):
            if board[i][j] == "R":  
                if rook_attack(board, i, j, king_row, king_col):
                    return True
            elif board[i][j] == "B":    
                if bishop_attack(board, i, j, king_row, king_col):
                    return True
            elif board[i][j] == "Q":
                if queen_attack(board, i, j, king_row, king_col):
                    return True 
            elif board[i][j] == "P":
                if pawn_attack(board, i, j, king_row, king_col):
                    return True
            else:
                continue
    return False

def rook_attack(board, rook_row, rook_col, king_row, king_col):
    if rook_row == king_row:
        for column in range(min(rook_col, king_col) + 1, max(rook_col, king_col)):
            if board[rook_row][column] != ".":
                return False
        return True
    elif rook_col == king_col:
        for row in range(min(rook_row, king_row) + 1, max(rook_row, king_row)):
            if board[row][rook_col] != ".":
                return False
        return True
    return False

def bishop_attack(board, bishop_row, bishop_col, king_row, king_col):
    if abs(bishop_row - king_row) == abs(bishop_col - king_col):
        row_step = 1 if king_row > bishop_row else -1
        col_step = 1 if king_col > bishop_col else -1
        row, column = bishop_row + row_step, bishop_col + col_step
        while row != king_row and column != king_col:
            if board[row][column] != ".":
                return False
            row += row_step
            column += col_step
        return True
    return False

def queen_attack(board, queen_row, queen_col, king_row, king_col):
    return rook_attack(board, queen_row, queen_col, king_row, king_col) or bishop_attack(board, queen_row, queen_col, king_row, king_col)

def pawn_attack(board, pawn_row, pawn_col, king_row, king_col):
    if pawn_row - 1 == king_row and (pawn_col - 1 == king_col or pawn_col + 1 == king_col):
        return True
    return False

def king_checkmate(board, king_row, king_col, rows, cols):
    if not check(board, king_row, king_col, rows): 
        return False

    king_moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    for r, c in king_moves:
        n_row = king_row + r
        n_col = king_col + c

        if (0 <= n_row < rows) and (0 <= n_col < cols):
            prev_piece = board[n_row][n_col]

            if prev_piece == '.':
                board[king_row][king_col] = '.'
                board[n_row][n_col] = 'K'

                checked = check(board, n_row, n_col, rows) 

                board[king_row][king_col] = 'K'
                board[n_row][n_col] = prev_piece

                if not checked:
                    return False
    
    return True

boardd = """\
K...
..P.
R...
...B\
"""

checkmate(boardd)
