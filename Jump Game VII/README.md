[Back to Table of Contents](../README.md)

# Jump Game VII
Difficulty: Medium

## Question
Jump Game VII
Attempted
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length

## Solution Template
```python
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
```
