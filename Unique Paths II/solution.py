class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid[n-1][m-1] == 1:
            return 0

        def rec(i, j):
            if i == n-1 and j == m-1:
                return 1
            
            if i < 0 or i >= n or \
               j < 0 or j >= m or \
               obstacleGrid[i][j]:
               return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            r = rec(i + 1, j)
            d = rec(i, j + 1)

            memo[(i,j)] = r + d

            return r+ d
        
        return rec(0, 0)

        