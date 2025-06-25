#check square
#check only one king
#check only allowed peices
#check board exists

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
        if num_rows != num_column:
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
        
        print("Success")
        
        if king_checkmate(board, king_row , king_col):
            print("Success")
            return
        else:
            print("Fail")
            return
    except:

        print("Fail")
        return
    


def is_in_check(board, king_row, king_col):

    for i in range(len(board)):
        for j in range(len(board)):
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
        for c in range(min(rook_col, king_col) + 1, max(rook_col, king_col)):
            if board[rook_row][c] != ".":
                return False
        return True
    elif rook_col == king_col:
        for r in range(min(rook_row, king_row) + 1, max(rook_row, king_row)):
            if board[r][rook_col] != ".":
                return False
        return True
    return False

def bishop_attack(board, bishop_row, bishop_col, king_row, king_col):


def queen_attack(board, queen_row, queen_col, king_row, king_col):
    return rook_attack(board, queen_row, queen_col, king_row, king_col) or bishop_attack(board, queen_row, queen_col, king_row, king_col)

def pawn_attack(board, pawn_row, pawn_col, king_row, king_col):
    if pawn_row + 1 == king_row and (pawn_col - 1 == king_col or pawn_col + 1 == king_col):
        return True
    return False

                
boardd = """
R...
.K..
..P.
....
"""

checkmate(boardd)




