[Back to Table of Contents](../README.md)

# Minimum Path Sum
Difficulty: Medium

## Question
Minimum Path Sum
Solved
Medium
Topics
premium lock icon
Companies
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200

## Solution Template
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        memo = {}

        def rec(i,j):
            if i == n-1 and j == m-1:
                return grid[i][j]
            if i < 0 or i >= n or \
               j < 0 or j >= m:
               return 1000000
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            r = rec(i+1,j)
            d = rec(i,j+1)

            memo[(i,j)] = min(r,d) + grid[i][j]
            return memo[(i,j)]
        

        return rec(0,0)
```
