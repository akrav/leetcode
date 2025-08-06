[Back to Table of Contents](../../README.md)

# Climbing Stairs
Difficulty: Easy

## Question
Climbing Stairs
Solved 
You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:

Input: n = 2

Output: 2
Explanation:

1 + 1 = 2
2 = 2
Example 2:

Input: n = 3

Output: 3
Explanation:

1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3
Constraints:

1 <= n <= 30

## Solution Template
```python
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         count = 0
#         prev_one = 0
#         prev_two = 1
#         for i in range(0,n):
#             count = prev_one + prev_two

#             prev_one = prev_two
#             prev_two = count
        
#         return count

class Solution:
    def climbStairs(self, n: int) -> int:

        def rec(num):
            if num < 0:
                return 0
            if num == 0:
                return 1
            
            op_one = rec(num-1)
            op_two = rec(num-2)

            return op_one + op_two
        
        return rec(n)

```
