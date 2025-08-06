[Back to Table of Contents](../README.md)

# Partition Labels
Difficulty: Medium

## Question
Partition Labels
Solved 
You are given a string s consisting of lowercase english letters.

We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

Return a list of integers representing the size of these substrings in the order they appear in the string.

Example 1:

Input: s = "xyxxyzbzbbisl"

Output: [5, 5, 1, 1, 1]
Explanation: The string can be split into ["xyxxy", "zbzbb", "i", "s", "l"].

Example 2:

Input: s = "abcabc"

Output: [6]
Constraints:

1 <= s.length <= 100

## Solution Template
```python
# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         #find the first letter 
#         #find the last position of the first in the string
#         #check all letters in substring
#         #from right find first appearance of one of the letters in the substring
#         #and thats the substring
#         # remove substring found
#         # repeat until no letters are left in s
#         ans = []
#         while s != '':
#             left = 0
#             right = len(s)-1

#             while left < right and s[left] != s[right]:
#                 right -= 1
            
#             dic = {}
#             for i in range(left, right + 1):
#                 dic[s[i]] = True
            
#             left = 0
#             right = len(s)-1
            
#             print(dic)
#             while left < right and s[right] not in dic.keys():
#                 right -= 1
#             ans.append(right-left+1)
#             s = s[right+1:]
        
#         return ans
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = defaultdict(int)

        for i in range(len(s)):
            last_index[s[i]] = max(last_index[s[i]], i)
        
        print(last_index)
        
        count = 1
        curr = 0
        end = 0
        ans = []
        while curr < len(s):
            curr_letter = s[curr]
            end = max(end, last_index[curr_letter])
            if curr == end:
                ans.append(count)
                count = 0
            curr += 1
            count += 1 
        
        return ans

```
