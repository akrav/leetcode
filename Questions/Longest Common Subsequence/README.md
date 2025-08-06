[Back to Table of Contents](../../README.md)

# Longest Common Subsequence
Difficulty: Medium

## Question
Longest Common Subsequence
Solved 
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Example 1:

Input: text1 = "cat", text2 = "crabt" 

Output: 3 
Explanation: The longest common subsequence is "cat" which has a length of 3.

Example 2:

Input: text1 = "abcd", text2 = "abcd"

Output: 4
Example 3:

Input: text1 = "abcd", text2 = "efgh"

Output: 0
Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

## Solution Template
```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        grid = [[0 for _ in range(n+1)] for _ in range(m+1)]


        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1] :
                    grid[i][j] = grid[i-1][j-1] + 1
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])

        return grid[m][n]

# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         def rec(i, j):
#             if i >= len(text1) or j >= len(text2):
#                 return 0

#             if text1[i] == text2[j]:
#                 return 1 + rec(i + 1, j + 1)
            
#             return max(rec(i + 1, j), rec(i, j + 1))
        
#         # Start the recursion from the beginning of both strings.
#         return rec(0, 0)

   

#     c.    r.  a.  b.  t
# c.  1.    1.  1.  1.  1

# a.  1.    1.  2.  2.  2

# t.  1.    1   2.  2.  3
```
