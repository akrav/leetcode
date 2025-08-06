[Back to Table of Contents](../../README.md)

# Interleaving String
Difficulty: Medium

## Question
Interleaving String
Solved 
You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met

|n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...
You may assume that s1, s2 and s3 consist of lowercase English letters.

Example 1:



Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

Output: true
Explanation: We can split s1 into ["aa", "aa"], s2 can remain as "bbbb" and s3 is formed by interleaving ["aa", "aa"] and "bbbb".

Example 2:

Input: s1 = "", s2 = "", s3 = ""

Output: true
Example 3:

Input: s1 = "abc", s2 = "xyz", s3 = "abxzcy"

Output: false
Explanation: We can't split s3 into ["ab", "xz", "cy"] as the order of characters is not maintained.

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200

## Solution Template
```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        o = len(s3)

        if n + m != o:
            return False
        
        def rec(i, j, path):
            if path != s3[:len(path)]:
                return False
            if i >= n and j >= m:
                if path == s3:
                    return True
                return False

            res = False
            if i < n :
                s3_idx = i + j

                path = path + s1[i]
                res = res or rec(i + 1, j, path)
                path = path[:-1]

            if j < m:
                path = path + s2[j]
                res = res or rec(i, j + 1, path)
                path = path[:-1]

            
            return res

        return rec(0, 0, '')
            
            
```
