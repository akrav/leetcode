[Back to Table of Contents](../../README.md)

# Plus One
Difficulty: Easy

## Question
Plus One
Solved 
You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:

Input: digits = [1,2,3,4]

Output: [1,2,3,5]
Explanation 1234 + 1 = 1235.

Example 2:

Input: digits = [9,9,9]

Output: [1,0,0,0]
Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9

## Solution Template
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        next_power = [1]
        carry = 1
        for i in range(n-1,-1,-1):
            new_digit = digits[i] + carry

            remainder = new_digit % 10
            carry = new_digit // 10
            digits[i] = remainder
        
        if carry == 1:
            return next_power + digits
        return digits
```
