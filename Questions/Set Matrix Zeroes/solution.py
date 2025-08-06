class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        is_first_row_zero = 1
        
        for i in range(num_rows):
            for j in range(num_cols):
                if matrix[i][j] == 0:
                    if i == 0:
                        is_first_row_zero = 0
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0


        is_first_col_zero = matrix[0][0]
        for i in range(num_rows-1, 0, -1):
            for j in range(num_cols-1, -1, -1): 
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        

        if is_first_row_zero == 0:
            for j in range(num_cols):
                matrix[0][j] = 0        
        
        