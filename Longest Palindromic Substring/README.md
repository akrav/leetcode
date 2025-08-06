[Back to Table of Contents](../README.md)

# Longest Palindromic Substring
Difficulty: Medium

## Question
Longest Palindromic Substring
Solved 
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:

Input: s = "ababd"

Output: "bab"
Explanation: Both "aba" and "bab" are valid answers.

Example 2:

Input: s = "abbc"

Output: "bb"
Constraints:

1 <= s.length <= 1000
s contains only digits and English letters.

## Solution Template
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        def is_pal(left, right):
            max_string = ''
            while left >= 0 and right <= len(s)-1:
                if s[left] != s[right]:
                    return max_string
                
                max_string = s[left:right+1]

                left -= 1
                right += 1
            
            return max_string
        
        
        m_string = is_pal(0, 0)
        for i in range(1, len(s)):
            candidate_one = is_pal(i, i)
            candidate_two = is_pal(i-1, i)

            if len(candidate_one) > len(candidate_two) and len(candidate_one) > len(m_string):
                m_string = candidate_one
            elif len(candidate_two) > len(candidate_one) and len(candidate_two) > len(m_string):
                m_string = candidate_two

        return m_string
```
