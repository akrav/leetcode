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