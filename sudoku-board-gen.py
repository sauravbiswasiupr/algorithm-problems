class Solution:
    def find_empty_location(self, arr, l): 
        for row in range(9): 
            for col in range(9): 
                if(arr[row][col]== "."): 
                    l[0]= row 
                    l[1]= col 
                    return True
        return False
  
   
    def used_in_row(self, arr, row, num): 
        for i in range(9): 
            if(arr[row][i] == str(num)): 
                return True
        return False
  
    
    def used_in_col(self, arr, col, num): 
        for i in range(9): 
            if(arr[i][col] == str(num)): 
                return True
        return False
  
   
    def used_in_box(self, arr, row, col, num): 
        for i in range(3): 
            for j in range(3): 
                if(arr[i + row][j + col] == str(num)): 
                    return True
        return False
  

    def check_location_is_safe(self, arr, row, col, num): 

        # Check if 'num' is not already placed in current row, 
        # current column and current 3x3 box 
        return not self.used_in_row(arr, row, num) and not self.used_in_col(arr, col, num) and not self.used_in_box(arr, row - row % 3, col - col % 3, num) 
  
 
    def solve_sudoku(self, arr): 

        # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
        l =[0, 0] 

        # If there is no unassigned location, we are done     
        if(not self.find_empty_location(arr, l)): 
            return True

        # Assigning list values to row and col that we got from the above Function  
        row = l[0] 
        col = l[1] 

        # consider digits 1 to 9 
        for num in range(1, 10): 

            # if looks promising 
            if(self.check_location_is_safe(arr, row, col, num)): 

                # make tentative assignment 
                arr[row][col]= str(num)

                if(self.solve_sudoku(arr)): 
                    return True

                # failure, unmake & try again 
                arr[row][col] = "."

        # this triggers backtracking         
        return False 

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve_sudoku(board)


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    sol = Solution()
    sol.solveSudoku(board)
    print(board)