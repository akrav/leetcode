[Back to Table of Contents](../README.md)

# Minimum Window Substring
Difficulty: Hard

## Question
Minimum Window Substring
Solved 
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""
Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.

## Solution Template
```python
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         t_dic = defaultdict(int)
#         s_dic = defaultdict(int)
        
#         def compare(tcom, scom):
#             for letter in t:
#                 if t_dic[letter] > s_dic[letter]:
#                     return False
#             return True
        
#         for letter in t:
#             t_dic[letter] += 1
#         left = 0
#         res = ''
#         min_res = ''
#         for right in range(len(s)):
#             res += s[right]
#             s_dic[s[right]] += 1
            
#             comp_res = compare(t_dic, s_dic)
#             while compare(t_dic, s_dic):
#                 if min_res == '':
#                     min_res = res
#                 elif min_res != '' and len(res) < len(min_res):
#                     min_res = res
                
#                 s_dic[s[left]] -= 1
#                 res = res[1:]
#                 left += 1

#         return min_res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dic = defaultdict(int)
        s_dic = defaultdict(int)
        
        def compare(tcom, scom):
            for letter in t:
                if t_dic[letter] > s_dic[letter]:
                    return False
            return True
        
        for letter in t:
            t_dic[letter] += 1
        need = len(t_dic)
        left = 0
        res = ''
        min_res = ''
        have = 0
        for right in range(len(s)):
            res += s[right]
            s_dic[s[right]] += 1
            if s_dic[s[right]] == t_dic[s[right]]:
                have += 1
            
            
            while have == need:
                print(f"have: {have}, need: {need}, res: {res}")
                if min_res == '':
                    min_res = res
                elif min_res != '' and len(res) < len(min_res):
                    min_res = res
                
                
                if s[left] in t_dic.keys():
                    if s_dic[s[left]] == t_dic[s[left]]:
                        have -= 1
                        
                s_dic[s[left]] -= 1
                res = res[1:]
                left += 1

        return min_res
                    
                    
                    
                    
```
