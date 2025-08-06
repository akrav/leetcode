class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def rec(i, j):
            if i < 0 or i >= m or \
               j < 0 or j >= n:
               return 0
            if i == m-1 and j == n-1:
                return 1
            
            right = rec(i, j + 1)
            down = rec(i + 1, j)

            return right + down
        
        return rec(0, 0)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[m-1][n-1]

# 1. 1.  1. 1.   1    1    1     1 
# 1  2   3  4.   5    6    7.    8
# 1  3.  6. 10   15   21   28    36
# 1. 4  10. 20   35   56   84    120
# 1. 5. 15  35   70   126  210.  330
# 1  6. 21  56.  126  252. 462.  792
# 1. 7. 28. 84.  210. 462. 924   1716
# 1. 8. 36. 120. 330  792  1716  3432