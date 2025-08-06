[Back to Table of Contents](../README.md)

# Longest Increasing Path in Matrix
Difficulty: Hard

## Question
Longest Increasing Path in Matrix
Solved 
You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.

Return the length of the longest strictly increasing path within matrix.

From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.

Example 1:



Input: matrix = [[5,5,3],[2,3,6],[1,1,1]]

Output: 4
Explanation: The longest increasing path is [1, 2, 3, 6] or [1, 2, 3, 5].

Example 2:



Input: matrix = [[1,2,3],[2,1,4],[7,6,5]]

Output: 7
Explanation: The longest increasing path is [1, 2, 3, 4, 5, 6, 7].

Constraints:

1 <= matrix.length, matrix[i].length <= 100

## Solution Template
```python
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
```
