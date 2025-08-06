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
        