[Back to Table of Contents](../README.md)

# Palindrome Partitioning
Difficulty: Medium

## Question
Palindrome Partitioning
Solved 
Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:

Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"

Output: [["a"]]
Constraints:

1 <= s.length <= 20
s contains only lowercase English letters.

## Solution Template
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []

        def is_palindrome(word):
            l = 0
            r = len(word) - 1

            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        def dfs_combination_split(path, word):
            if word == "":
                self.res.append(path[:])
                return
            
            for i in range(1, len(word)+1):
                new_word = word[:i]

                if not is_palindrome(new_word):
                    continue
                
                path.append(new_word)
                dfs_combination_split(path, word[i:])
                path.pop()
        
        dfs_combination_split([], s)
        return self.res


        
```
