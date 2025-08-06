[Back to Table of Contents](../README.md)

# Counting Bits
Difficulty: Easy

## Question
Counting Bits
Solved 
Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 4

Output: [0,1,1,2,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100

Constraints:

0 <= n <= 1000

## Solution Template
```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            m = i
            while m != 0:
                count += m%2
                m = m >> 1
            res.append(count)
        return res
            
```
