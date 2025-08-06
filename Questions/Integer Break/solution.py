# class Solution:
#     def integerBreak(self, n: int) -> int:
#         if n == 2:
#             return 1
#         if n == 3:
#             return 2

#         max_prod = n-1
#         def rec(start, m, prod):
#             nonlocal max_prod
#             if m == 0:
#                 max_prod = max(max_prod, prod)
#                 return
#             if m < 0:
#                 return
#             for i in range(start, m+1):
#                 rec(i, m - i, prod * i)
            
#             return
        
#         rec(1, n, 1)
#         return max_prod


# class Solution:
#     def integerBreak(self, n: int) -> int:
#         # Memo to avoid recomputing
#         memo = {}

#         def dfs(x: int) -> int:
#             # If we've already computed the best for x
#             if x in memo:
#                 return memo[x]

#             # For x <= 2, the best product is x-1 
#             # (this enforces at least one break)
#             if x <= 2:
#                 return x - 1

#             best = 0
#             # Try breaking x into i + (x - i)
#             for i in range(1, x):
#                 # Either take i * (x - i) or i * dfs(x - i)
#                 # The max ensures we consider further breaks vs. no further breaks
#                 best = max(best, i * (x - i), i * dfs(x - i))

#             memo[x] = best
#             return best

#         return dfs(n)






class Solution:
    def integerBreak(self, n: int) -> int:

        max_prod = n-1
        def rec(start, m, prod, count):
            nonlocal max_prod
            if m == 0 and count >= 2:
                max_prod = max(max_prod, prod)
                return
            if m < 0:
                return
            for i in range(start, m+1):
                rec(i, m - i, prod * i, count+1)
            
            return
        
        rec(1, n, 1, 0)
        return max_prod