[Back to Table of Contents](../../README.md)

# Perfect Squares
Difficulty: Medium

## Question
Perfect Squares
Solved
Medium
Topics
premium lock icon
Companies
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 104

## Solution Template
```python
class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_n = math.floor(n ** (1/2))
        min_count = 100000

        def rec(end, target, count):
            nonlocal min_count
            if target == 0:
                min_count = min(min_count, count)
                return 
            if target < 0:
                return 
            if count >= min_count:
                return
            
            for i in range(end, 0, -1):
                rec(i, target - i**2, count + 1)

            return 
        rec(sqrt_n, n, 0)
        return min_count
```
