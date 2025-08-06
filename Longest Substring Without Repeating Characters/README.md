[Back to Table of Contents](../README.md)

# Longest Substring Without Repeating Characters
Difficulty: Medium

## Question
Longest Substring Without Repeating Characters
Solved 
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.

## Solution Template
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        alpha = defaultdict(lambda: -1)

        left = 0
        right = 0

        max_length = 0
        while right < len(s):
            letter = s[right]

            if alpha[letter] == -1:
                alpha[letter] = right
            else:
                left = max(left, alpha[letter] + 1)
                alpha[letter] = right
            print(f"left: {left}, right: {right}, (right - left): {(right - left)}, max_length: {max_length}")
            max_length = max(max_length, (right - left) + 1)
            print(f"left: {left}, right: {right}, (right - left): {(right - left)}, max_length: {max_length}")

            right += 1
        
        return max_length
```
