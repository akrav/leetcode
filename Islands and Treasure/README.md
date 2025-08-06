[Back to Table of Contents](../README.md)

# Islands and Treasure
Difficulty: Medium

## Question
Islands and Treasure
Solved 
You are given a 
m
×
n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:

Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
Example 2:

Input: [
  [0,-1],
  [2147483647,2147483647]
]

Output: [
  [0,-1],
  [1,2]
]
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}

## Solution Template
```python
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.n = len(grid)
        self.m = len(grid[0])

        def dfs(i, j, depth, visited):
            if i < 0 or i >= self.n or \
               j < 0 or j >= self.m:
               return
            if grid[i][j] == -1:
                return
            if f'{i},{j}' in visited.keys() and depth >= grid[i][j]:
                return

            visited[f'{i},{j}'] = True
            grid[i][j] = min(grid[i][j], depth)
            dfs(i + 1, j, depth + 1, visited)
            dfs(i - 1, j, depth + 1, visited)
            dfs(i, j + 1, depth + 1, visited)
            dfs(i, j - 1, depth + 1, visited)
            visited[f'{i},{j}'] = False


        

        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 0:
                    dfs(i, j, 0, {})
        
        
```
