class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        def rec(m):
            if m in memo:
                return memo[m]
            if m == 0:
                return 0
            if m <= 2:
                return 1
            
            memo[m] = rec(m-1) + rec(m-2) + rec(m-3)
            return memo[m]
        
        return rec(n)


# class Solution:
#     def tribonacci(self, n: int) -> int:
#         memo = {}
        
#         def helper(n):
#             if n in memo:
#                 return memo[n]
#             if n == 0:
#                 return 0
#             elif n == 1 or n == 2:
#                 return 1
#             else:
#                 result = helper(n - 1) + helper(n - 2) + helper(n - 3)
#                 memo[n] = result
#                 return result
        
#         return helper(n)