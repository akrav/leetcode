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
        