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
            board.append(r)
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
                if board[i][j] != "K" or board[i][j] != "P" or board[i][j] != "Q" or board[i][j] != "R" or board[i][j] != "B" or board[i][j] != ".":
                    print("Fail")
                    return
                elif board[i][j] == "K":
                    king_count += 1
                    king_row , king_col = i , j
        
        if king_count > 1:
            print("Fail")
            return
        
        if king_checkmate(board, king_row , king_col):
            print("Success")
            return
        else:
            print("Fail")
            return
    except:

        print("Fail")
        return
    
def king_checkmate(board, row, col):


