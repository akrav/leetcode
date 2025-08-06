[Back to Table of Contents](../../README.md)

# Spiral Matrix
Difficulty: Medium

## Question
Spiral Matrix
Solved 
Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.

Example 1:



Input: matrix = [[1,2],[3,4]]

Output: [1,2,4,3]
Example 2:



Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [1,2,3,6,9,8,7,4,5]
Example 3:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]
Constraints:

1 <= matrix.length, matrix[i].length <= 10
-100 <= matrix[i][j] <= 100

## Solution Template
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = m
        bottom = 0
        up = n

        ans = []
        while left < right and bottom < up:
            for i in range(left, right):
                ans.append(matrix[bottom][i])
            bottom += 1

            for i in range(bottom, up):
                ans.append(matrix[i][right-1])
            right -= 1

            if left >= right or bottom >= up:
                break
                
            for i in range(right-1, left-1, -1):
                ans.append(matrix[up-1][i])
            up -= 1


            for i in range(up -1, bottom -1, -1):
                ans.append(matrix[i][left])
            left += 1

        return ans
```
