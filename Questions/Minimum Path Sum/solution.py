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