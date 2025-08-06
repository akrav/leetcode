[Back to Table of Contents](../../README.md)

# Edit Distance
Difficulty: Medium

## Question
Edit Distance
Solved 
You are given two strings word1 and word2, each consisting of lowercase English letters.

You are allowed to perform three operations on word1 an unlimited number of times:

Insert a character at any position
Delete a character at any position
Replace a character at any position
Return the minimum number of operations to make word1 equal word2.

Example 1:

Input: word1 = "monkeys", word2 = "money"

Output: 2
Explanation:
monkeys -> monkey (remove s)
monkey -> monkey (remove k)

Example 2:

Input: word1 = "neatcdee", word2 = "neetcode"

Output: 3
Explanation:
neatcdee -> neetcdee (replace a with e)
neetcdee -> neetcde (remove last e)
neetcde -> neetcode (insert o)

Constraints:

0 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

## Solution Template
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        
        n = len(word1)
        m = len(word2)
        memo = {}
        def rec(i, j):
            if i == n:
                return m - j
            
            if j == m:
                return n - i
            
            if (i,j) in memo:
                return memo[(i,j)]
            
            res = 10000000
            if word1[i] == word2[j]:
                res = rec(i + 1, j + 1)
            else:
                res = min(res, rec(i + 1, j), rec(i, j + 1), rec(i + 1, j + 1)) + 1
            
            memo[(i,j)] = res
            
            return res 
        
        return rec(0,0)
```
