[Back to Table of Contents](../../README.md)

# Sum of Two Integers
Difficulty: Medium

## Question
Sum of Two Integers
Solved 
Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:

Input: a = 1, b = 1

Output: 2
Example 2:

Input: a = 4, b = 7

Output: 11
Constraints:

-1000 <= a, b <= 1000

## Solution Template
```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            c  = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = c
        
        return a if a <= max_int else ~(a ^ mask)
        
```
