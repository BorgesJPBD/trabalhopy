def is_valid_sudoku(board):
    for i in range(9):
        
        if len(set(board[i])) != len([x for x in board[i] if x != 0]):
            return False
        if len(set(board[j][i] for j in range(9))) != len([x for x in (board[j][i] for j in range(9)) if x != 0]):
            return False
        
        
        row_start, col_start = (i // 3) * 3, (i % 3) * 3
        subgrid = [board[row_start + r][col_start + c] for r in range(3) for c in range(3) if board[row_start + r][col_start + c] != 0]
        if len(set(subgrid)) != len(subgrid):
            return False
    
    return True


sudoku_board = [
    [5, 3, 0, 0, 7, 9, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 6, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 7, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


if is_valid_sudoku(sudoku_board):
    print("O Sudoku é válido.")
else:
    print("O Sudoku não é válido.")