[Back to Table of Contents](../README.md)

# Search a 2D Matrix
Difficulty: Medium

## Question
Search a 2D Matrix
Solved 
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
Example 2:



Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

Output: false
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000

## Solution Template
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search row
        low = 0
        high = len(matrix) -1

        while low < high:
            mid = low + (high - low) // 2

            if target > matrix[mid][-1]:
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                high = mid
        
        row = high

        # binary search col
        left = 0
        right = len(matrix[0]) - 1

        while left < right:
            mid = left + (right - left) // 2

            if target > matrix[row][mid]:
                left = mid + 1
            else:
                right = mid
        
        col = right

        return True if matrix[row][col] == target else False
```
