[Back to Table of Contents](../../README.md)

# Reverse Bits
Difficulty: Easy

## Question
Reverse Bits
Solved 
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:

Input: n = 00000000000000000000000000010101

Output:    2818572288 (10101000000000000000000000000000)
Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.

## Solution Template
```python
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            # get first number & with 1 to get the bit at the last position
            # ex 5 101  we want to check what the last 1 is
            # 1 & 1 is 1
            # move value to the end of the bit ar idx 31 below and continue
            res += (bit << (31 - i))
        return res
```
