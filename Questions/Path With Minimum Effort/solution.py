# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         n = len(heights)
#         m = len(heights[0])
#         memo = {}
#         visited = {}
#         def rec(i,j):
#             if i == n-1 and j == m-1:
#                 return heights[i][j]
#             if i < 0 or i >= n or \
#                j < 0 or j >= m:
#                return 100000
#             if (i,j) in memo:
#                 return memo[(i,j)]
#             u =100000
#             d =100000
#             r =100000
#             l =100000
#             if (i-1,j) not in visited or visited[(i-1,j)] == False:
#                 visited[(i-1,j)] = True
#                 u = rec(i-1,j)
#                 visited[(i-1,j)] = False

#             if (i+1,j) not in visited or visited[(i+1,j)] == False:
#                 visited[(i+1,j)] = True
#                 d = rec(i+1,j)
#                 visited[(i+1,j)] = False
            
#             if (i,j-1) not in visited or visited[(i,j-1)] == False:
#                 visited[(i,j-1)] = True
#                 l = rec(i,j-1)
#                 visited[(i,j-1)] = False
            
#             if (i,j+1) not in visited or visited[(i,j+1)] == False:
#                 visited[(i-1,j)] = True
#                 r = rec(i,j+1)
#                 visited[(i-1,j)] = False

#             memo[(i,j)] = heights[i][j] + min(u,d,r,l)

#             return heights[i][j] + min(u,d,r,l)
        
#         return rec(0,0)

import heapq as hq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        visited = {}
        pq = [[0,0,0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while pq:
            diff, r, c = hq.heappop(pq)

            if (r,c) in visited and visited[(r,c)] == True:
                continue
            visited[(r,c)] = True

            if r == (n-1) and c == (m-1):
                return diff
            
            for dr, dc in directions:
                new_row = r + dr
                new_col = c +dc

                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m or ((new_row, new_col) in visited and visited[(new_row, new_col)] == True):
                    continue
                
                hq.heappush(pq, [max(diff, abs(heights[r][c] - heights[new_row][new_col])), new_row, new_col])
        return 0
