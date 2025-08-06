[Back to Table of Contents](../README.md)

# Permutation in String
Difficulty: Medium

## Question
Permutation in String
Solved 
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false
Constraints:

1 <= s1.length, s2.length <= 1000

## Solution Template
```python
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         n = len(s1)
#         word_dic = defaultdict(int)

#         for letter in s1:
#             word_dic[letter] += 1
        
#         def check_solutions(word_dic, s):
#             for letter in s:
#                 if word_dic[letter] != 0:
#                     return False
#             return True
        
#         left = 0
#         right = 0
#         word_dic[s2[right]] -= 1


#         while right < len(s2):
#             print(f"s1: {s1}, s2: {s2[left:right+1]}")
#             if right - left + 1 == len(s1):
#                 print(f"word_dic: {word_dic}")
#                 if check_solutions(word_dic, s1):
#                     return True
#                 right += 1
#                 if right  >= len(s2):
#                     return False
#                 letter_add = s2[right]
#                 letter_removed = s2[left]
#                 word_dic[letter_add] -= 1
#                 word_dic[letter_removed] += 1
#                 left += 1
#             elif right - left < len(s1): 
#                 print(f"moving right pointer")
#                 right += 1
#                 if right  >= len(s2):
#                     return False
#                 letter_add = s2[right]
#                 word_dic[letter_add] -= 1
#             else:
#                 print(f"moving left pointer")
#                 letter_removed = s2[left]
#                 word_dic[letter_removed] += 1
#                 left += 1
        
#         return False

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_dic = defaultdict(int)
        s2_dic = defaultdict(int)

        matches = 0

        for i in range(len(s1)):
            s1_dic[s1[i]] += 1
            s2_dic[s2[i]] += 1
        
        for i in range(26):
            letter = chr(ord('a') + i)
            if s1_dic[letter] == s2_dic[letter]:
                matches += 1
        
        left = 0
        right = len(s1)

        while right < len(s2):
            if matches == 26:
                return True
            
            letter_r = s2[right]
            letter_l = s2[left]

            s2_dic[letter_r] += 1
            if s2_dic[letter_r] == s1_dic[letter_r]:
                matches += 1
            elif s2_dic[letter_r]-1 == s1_dic[letter_r]:
                matches -= 1
            

            s2_dic[letter_l] -= 1
            if s2_dic[letter_l] == s1_dic[letter_l]:
                matches += 1
            elif s2_dic[letter_l]+1 == s1_dic[letter_l]:
                matches -= 1
            
            left += 1
            right += 1
        
        return matches == 26
```
