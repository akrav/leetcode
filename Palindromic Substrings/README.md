[Back to Table of Contents](../README.md)

# Palindromic Substrings
Difficulty: Medium

## Question
Palindromic Substrings
Solved 
Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: s = "abc"

Output: 3
Explanation: "a", "b", "c".

Example 2:

Input: s = "aaa"

Output: 6
Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

## Solution Template
```python
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def is_pal(word):
#             left = 0
#             right = len(word)-1

#             while left < right:
#                 if s[left] != s[right]:
#                     return False
                
#                 left += 1
#                 right -= 1
            
#             return True
        
#         self.paths = []
#         def combination(start, word):
#             if len(word) != 0 and is_pal(word):
#                 self.paths.append(word)
            
#             if start > len(s)-1:
#                 return
            
#             for i in range(start, len(s)):
#                 word = word + s[i]
#                 combination(i+1, word)
#                 word = word[:-1]
            
#             return

        
#         combination(0,'')
#         print(self.paths)
#         return len(self.paths)

class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_pal(word: str) -> bool:
            left, right = 0, len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        self.paths = []  # to store palindromic contiguous substrings
        
        # This recursive helper builds a contiguous substring starting at index `start`
        # by always appending the next character.
        def contiguous(start: int, word: str) -> None:
            if start >= len(s):
                return
            new_word = word + s[start]
            if is_pal(new_word):
                self.paths.append(new_word)
            # Only move to the next character (ensuring contiguity)
            contiguous(start + 1, new_word)
        
        # Try every possible starting index for a contiguous substring.
        for i in range(len(s)):
            contiguous(i, "")
        
        return len(self.paths)
```
