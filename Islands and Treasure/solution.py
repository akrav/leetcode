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
        
        