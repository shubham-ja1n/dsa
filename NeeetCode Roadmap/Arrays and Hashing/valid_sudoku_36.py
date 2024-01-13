def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    row_hash = {}
    col_hash = {}
    square_hash = {}

    for row in range(9):
        for col in range(9):
            if row not in row_hash:
                row_hash[row] = set()

            if col not in col_hash:
                col_hash[col] = set()

            if (row//3, col//3) not in square_hash:
                square_hash[(row//3, col//3)] = set()

            if board[row][col] == ".":
                continue
            
            if (board[row][col] in row_hash[row] or board[row][col] in col_hash[col] or board[row][col] in square_hash[(row//3,col//3)]):
                return False
            
            row_hash[row].add(board[row][col])
            col_hash[col].add(board[row][col])
            square_hash[(row//3,col//3)].add(board[row][col])
    return True