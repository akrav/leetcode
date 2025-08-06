[Back to Table of Contents](../../README.md)

# Number of Islands
Difficulty: Medium

## Question
Number of Islands
Solved 
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Example 1:

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1
Example 2:

Input: grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
Output: 4
Constraints:

1 <= grid.length, grid[i].length <= 100
grid[i][j] is '0' or '1'.

## Solution Template
```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])

        def dfs_remove_island(i, j):
            if i < 0 or i >= self.n or \
               j < 0 or j >= self.m:

               return
            
            val = grid[i][j]

            if val == "0" or val =="2":
                return 

            grid[i][j] = "2"
            dfs_remove_island(i + 1, j)
            dfs_remove_island(i - 1, j)
            dfs_remove_island(i, j + 1)
            dfs_remove_island(i, j - 1)

        count = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == "1":
                    count += 1
                    dfs_remove_island(i, j)
        
        return count
        
```
