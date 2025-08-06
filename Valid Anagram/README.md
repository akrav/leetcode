[Back to Table of Contents](../README.md)

# Valid Anagram   
Difficulty: Easy

## Question
Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

## Solution Template
```python
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_dic = defaultdict(int)

#         for letter in s:
#             s_dic[letter] += 1
        
#         for letter in t:
#             s_dic[letter] -= 1
#             if s_dic[letter] < 0:
#                 return False
        
#         for letter in s:
#             if s_dic[letter] != 0:
#                 return False
#         return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_dic[s[i]] += 1
            t_dic[t[i]] += 1
        
        for letter in s:
            if s_dic[letter] != t_dic[letter]:
                return False
        return True
        
```
