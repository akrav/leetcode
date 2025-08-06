# class Solution:
#     def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
#         n = len(s)-1
#         memo = {}

#         def rec(idx):
#             if idx == n:
#                 return True
            
#             if idx > n:
#                 return False
#             if idx in memo:
#                 return memo[idx]
            
#             ans = False
#             for i in range(maxJump, minJump-1, -1):
#                 new_idx = (idx + i)
#                 if new_idx > n  or s[new_idx] != '0':
#                     if  new_idx == n and  s[new_idx] != '0':
#                         memo[idx] = False
#                         return False
#                     continue
                
#                 if rec(new_idx):
#                     memo[idx] = True
#                     return True

            
#             memo[idx] = False
            
#             return False
        
#         return False if s[0] != '0' else rec(0)



class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [None] * n
        dp[n - 1] = True

        def dfs(i):
            if dp[i] is not None:
                return dp[i]

            dp[i] = False
            for j in range(i + minJump, min(n, i + maxJump + 1)):
                if s[j] == '0' and dfs(j):
                    dp[i] = True
                    break

            return dp[i]

        if s[-1] == '1':
            return False
        return dfs(0)