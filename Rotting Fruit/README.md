[Back to Table of Contents](../README.md)

# Rotting Fruit
Difficulty: Medium

## Question
Rotting Fruit
Solved 
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Example 1:



Input: grid = [[1,1,0],[0,1,1],[0,1,2]]

Output: 4
Example 2:

Input: grid = [[1,0,1],[0,2,0],[1,0,1]]

Output: -1
Constraints:

1 <= grid.length, grid[i].length <= 10

## Solution Template
```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0]) if self.n > 0 else 0
        
        # Count fresh oranges, gather all rotten oranges in a queue (multi-source BFS)
        queue = deque()  # will store tuples (row, col, time)
        fresh_count = 0
        
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    # This is a rotten orange, start BFS from here
                    queue.append((i, j, 0))  # time=0 for these initial rotten
        
        # If no fresh oranges from the start, answer is 0
        if fresh_count == 0:
            return 0
        
        # Directions for up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        final_time = 0  # track maximum minutes
        # BFS: process queue
        while queue:
            row, col, time = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                # check if valid cell and is fresh (==1)
                if 0 <= nr < self.n and 0 <= nc < self.m and grid[nr][nc] == 1:
                    # rot this fresh orange
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    new_time = time + 1
                    final_time = max(final_time, new_time)
                    # push the newly rotten orange into the queue
                    queue.append((nr, nc, new_time))
        
        # if any fresh oranges remain, return -1
        if fresh_count > 0:
            return -1
        else:
            return final_time
```
