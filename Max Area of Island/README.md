[Back to Table of Contents](../README.md)

# Max Area of Island
Difficulty: Medium

## Question
Max Area of Island
Solved 
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.

Example 1:



Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6
Explanation: 1's cannot be connected diagonally, so the maximum area of the island is 6.

Constraints:

1 <= grid.length, grid[i].length <= 50

## Solution Template
```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])

        def dfs_count_island(i,j):
            if i < 0 or i >= self.n or \
               j < 0 or j >= self.m:
               return 0

            val = grid[i][j]
            if val == 0 or val == 2:
                return 0
            
            grid[i][j] = 2
            u = dfs_count_island(i - 1, j)
            d = dfs_count_island(i + 1, j)
            l = dfs_count_island(i, j - 1)
            r = dfs_count_island(i, j + 1)

            return u + d + l + r + 1

        max_count = 0 
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    new_count = dfs_count_island(i,j)
                    max_count = max(max_count, new_count)
        
        return max_count
        
```
