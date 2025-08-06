[Back to Table of Contents](../../README.md)

# Word Break II
Difficulty: Hard

## Question
Word Break II
Solved
Hard
Topics
premium lock icon
Companies
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.

## Solution Template
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        
        ans = []
        def rec(idx, path):
            if idx == n:
                ans.append(" ".join(path[:]))
                return
            
            for end in range(idx, n):
                if not in_dic(idx, end):
                    continue
                
                path.append(s[idx:end+1])
                rec(end+1, path)
                path.pop()
            
            return
            
        def in_dic(start, end):
            if s[start:end+1] in wordDict:
                return True
            return False
        
        rec(0, [])
        return ans
```
