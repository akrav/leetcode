[Back to Table of Contents](../README.md)

# Greatest Common Divisor of Strings
Difficulty: Easy

## Question
Greatest Common Divisor of Strings
Solved
Easy
Topics
premium lock icon
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

## Solution Template
```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def is_Divisor(str_len):
            if len1 % str_len != 0 or len2 % str_len != 0:
                return False
            str1_num_of_repeats = len1//str_len
            str2_num_of_repeats = len2//str_len
            return ((str1[:str_len] * str1_num_of_repeats) == str1) and ((str1[:str_len] * str2_num_of_repeats) == str2)
        
        for i in range(min(len1, len2), 0, -1):
            if is_Divisor(i):
                return str1[:i]
        
        return ""
```
