class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        def gen_options(i,j,prev_val):
            all_options = [[1,0],[-1, 0], [0,1], [0,-1]]

            res = []
            for row, col in all_options:
                new_row = i + row
                new_col = j + col
                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
                    continue
                
                if matrix[new_row][new_col] <= prev_val:
                    continue
                
                res.append([row,col])
            
            return res

        
        def rec(i, j, prev_val, count):
            if i < 0 or i >= n or \
               j < 0 or j >= m:

               return 0

            path_options = gen_options(i,j, matrix[i][j])
            if len(path_options) == 0:
                return count
            
            max_depth = 0
            for row, col in path_options:
                max_depth = max(max_depth, rec(i + row, j + col, matrix[i][j], count + 1))
            
            return max_depth
        

        max_val = -10000
        for i in range(n):
            for j in range(m):
                max_val = max(max_val, rec(i, j, -100000, 1))
        
        return max_val