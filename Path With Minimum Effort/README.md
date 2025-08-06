[Back to Table of Contents](../README.md)

# Path With Minimum Effort
Difficulty: Medium

## Question
Path With Minimum Effort
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

## Solution Template
```python
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

```
