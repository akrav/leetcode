[Back to Table of Contents](../../README.md)

# Pacific Atlantic Water Flow
Difficulty: Medium

## Question
Pacific Atlantic Water Flow
Solved 
You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.

Example 1:



Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]

Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]
Example 2:

Input: heights = [[1],[1]]

Output: [[0,0],[0,1]]
Constraints:

1 <= heights.length, heights[r].length <= 100
0 <= heights[r][c] <= 1000

## Solution Template
```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.n = len(heights)
        self.m = len(heights[0])
        
        
        def dfs(i, j, prev_val, oceans_visited):
            if i < 0 or i >= self.n or \
               j < 0 or j >= self.m:
               return False
            
            if prev_val < heights[i][j]:
                return False
            
            if i == 0 or j == 0:
                oceans_visited["a"] = True
            
            if i == self.n - 1 or j == self.m - 1:
                oceans_visited["p"] = True
            
            if oceans_visited["a"] and oceans_visited["p"]:
                return True
            
            p_val = heights[i][j]
            heights[i][j] = 100000
            u = dfs(i - 1, j, p_val, oceans_visited)
            d = dfs(i + 1, j, p_val, oceans_visited)
            l = dfs(i, j - 1, p_val, oceans_visited)
            r = dfs(i, j + 1, p_val, oceans_visited)
            heights[i][j] = p_val


            return u or d or l or r
        
        ans = []
        for i in range(self.n):
            for j in range(self.m):
                oceans_visited = {
                    "a": False,
                    "p": False
                }
                
                if dfs(i, j, 1000000, oceans_visited):
                    ans.append([i,j])
        
        return ans
```
