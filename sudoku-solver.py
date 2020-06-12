def check_slice_has_non_unique_elements(slice):
    units = [j for j in slice if j != "."]
    if len(set(units)) != len(units):
        return True
    return False

def is_valid_sudoku(board):
    if not board:
        raise Exception("No input provided")

    for i in range(9):

        if check_slice_has_non_unique_elements(board[i]):
            return False
        
        if check_slice_has_non_unique_elements([board[k][i] for k in range(9)]):
            return False
        
    for i in [0, 3, 6]:
        for j in  [0, 3, 6]:
            grid_slice = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
            if check_slice_has_non_unique_elements(grid_slice):
                return False
    
    return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(is_valid_sudoku(board))