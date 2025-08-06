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