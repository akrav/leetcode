[Back to Table of Contents](../README.md)

# N-th Tribonacci Number
Difficulty: Easy

## Question
N-th Tribonacci Number
Solved
Easy
Topics
premium lock icon
Companies
Hint
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
 

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

## Solution Template
```python
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
```
