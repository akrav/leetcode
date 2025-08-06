class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= row or \
               c < 0 or c >= col or \
               grid[r][c] == 0:
               return 1
            if grid[r][c] == -1:
                return 0

            grid[r][c] = -1
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return up + down + left + right
        
        perimeter = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += dfs(i, j)
        
        return perimeter


# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#         perimeter = 0
        
#         def dfs(r, c):
#             if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
#                 return 1
#             if grid[r][c] == -1:
#                 return 0
#             grid[r][c] = -1
#             return (dfs(r + 1, c) +
#                     dfs(r - 1, c) +
#                     dfs(r, c + 1) +
#                     dfs(r, c - 1))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                     perimeter += dfs(r, c)

#         return perimeter