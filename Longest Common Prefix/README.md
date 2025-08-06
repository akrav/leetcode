[Back to Table of Contents](../README.md)

# Longest Common Prefix
Difficulty: Easy

## Question
Longest Common Prefix
Solved
Easy
Topics
premium lock icon
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.

## Solution Template
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 1:
            return '' if len(strs) == 0 else strs[0]
        
        prefix = strs[0]
        for i in range(1, len(strs)):
            new_prefix = ''
            for j in range(min(len(prefix), len(strs[i]))):
                if strs[i][j] != prefix[j]:
                    break
                new_prefix += strs[i][j]
            prefix = new_prefix
        
        return prefix
```
