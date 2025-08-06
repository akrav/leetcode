[Back to Table of Contents](../README.md)

# Reverse Integer
Difficulty: Medium

## Question
Reverse Integer
Solved 
You are given a signed 32-bit integer x.

Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

Solve the problem without using integers that are outside the signed 32-bit integer range.

Example 1:

Input: x = 1234

Output: 4321
Example 2:

Input: x = -1234

Output: -4321
Example 3:

Input: x = 1234236467

Output: 0
Constraints:

-2^31 <= x <= 2^31 - 1

## Solution Template
```python
class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647

        res = 0
        while x != 0:
            # mode and floor divide work poorly with negative numbers in python
            # these functions help
            digit = int(math.fmod(x,10)) 
            x = int(x/10)

            if res > MAX//10 or (res == MAX//10 and digit >= MAX % 10):
                return 0
            if res < int(MIN/10) or (res == int(MIN/10) and digit <= int(math.fmod(MIN,10)) ):
                return 0
            res = res * 10 + digit

        return res
```
