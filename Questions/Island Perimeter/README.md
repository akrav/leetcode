[Back to Table of Contents](../../README.md)

# Island Perimeter
Difficulty: Easy

## Question
Island Perimeter
Solved
Easy
Topics
premium lock icon
Companies
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.

## Solution Template
```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= row or \
               c < 0 or c >= col or \
               grid[r][c] == 0:
               return 1
            if grid[r][c] == -1:
                return 0

            grid[r][c] = -1
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return up + down + left + right
        
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += dfs(i, j)
        
        return perimeter


# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#         perimeter = 0
        
#         def dfs(r, c):
#             if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
#                 return 1
#             if grid[r][c] == -1:
#                 return 0
#             grid[r][c] = -1
#             return (dfs(r + 1, c) +
#                     dfs(r - 1, c) +
#                     dfs(r, c + 1) +
#                     dfs(r, c - 1))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                     perimeter += dfs(r, c)

#         return perimeter
```
