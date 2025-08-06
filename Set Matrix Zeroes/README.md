[Back to Table of Contents](../README.md)

# Set Matrix Zeroes
Difficulty: Medium

## Question
Set Matrix Zeroes
Solved 
Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

Example 1:



Input: matrix = [
  [0,1],
  [1,0]
]

Output: [
  [0,0],
  [0,0]
]
Example 2:



Input: matrix = [
  [1,2,3],
  [4,0,5],
  [6,7,8]
]

Output: [
  [1,0,3],
  [0,0,0],
  [6,0,8]
]
Constraints:

1 <= matrix.length, matrix[0].length <= 100
-2^31 <= matrix[i][j] <= (2^31) - 1

## Solution Template
```python
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
        
        
```
