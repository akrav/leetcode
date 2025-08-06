[Back to Table of Contents](../README.md)

# Transpose Matrix
Difficulty: Easy

## Question
Transpose Matrix
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.



 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109

## Solution Template
```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        tm = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
        # print(f"tm: {tm}")
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                tm[j][i] = matrix[i][j]
        
        return tm
```
