[Back to Table of Contents](../README.md)

# Rotate Image
Difficulty: Medium

## Question
Rotate Image
Solved 
Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.

Example 1:



Input: matrix = [
  [1,2],
  [3,4]
]

Output: [
  [3,1],
  [4,2]
]
Example 2:



Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

## Solution Template
```python
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix)
#         m = len(matrix[0])

#         print(f"before: {matrix}")
#         for i in range(n):
#             for j in range(i, m):
#                 matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
#         print(f"after: {matrix}")

#         for i in range(n):
#             left = 0
#             right = m - 1
#             while left < right:
#                 matrix[i][left], matrix[i][right]= matrix[i][right], matrix[i][left]
#                 left += 1
#                 right -= 1

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if i + j < n - 1:
                    matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]

        left = 0
        right = m - 1
        while left < right:
            matrix[left], matrix[right]= matrix[right], matrix[left]
            left += 1
            right -= 1

# before: [[1, 2, 3], 
#          [4, 5, 6], 
#          [7, 8, 9]]

# after: [[1, 4, 7], 
#         [2, 5, 8], 
#         [3, 6, 9]]

# after: [[9, 6, 3], 
#         [8, 5, 2], 
#         [7, 4, 1]]
```
