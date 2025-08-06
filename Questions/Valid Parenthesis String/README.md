[Back to Table of Contents](../../README.md)

# Valid Parenthesis String
Difficulty: Medium

## Question
Valid Parenthesis String
Solved 
You are given a string s which contains only three types of characters: '(', ')' and '*'.

Return true if s is valid, otherwise return false.

A string is valid if it follows all of the following rules:

Every left parenthesis '(' must have a corresponding right parenthesis ')'.
Every right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".
Example 1:

Input: s = "((**)"

Output: true
Explanation: One of the '*' could be a ')' and the other could be an empty string.

Example 2:

Input: s = "(((*)"

Output: false
Explanation: The string is not valid because there is an extra '(' at the beginning, regardless of the extra '*'.

Constraints:

1 <= s.length <= 100

## Solution Template
```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def rec(idx, open_count):
            if open_count < 0:
                return False
            if idx == len(s) and open_count == 0:
                return True
            if idx == len(s):
                return False
            if (idx, open_count) in memo:
                return memo[(idx, open_count)]
            
            val = s[idx]
            ans = False
            if val == "(":
                ans = rec(idx + 1, open_count + 1)
            elif val == ")":
                ans = rec(idx + 1, open_count - 1)
            else:
                # * is open parenthesis 
                op_1 = rec(idx + 1, open_count + 1)
                # * is clos parenthesis 
                op_2 = rec(idx + 1, open_count - 1)
                # * is empty string
                op_3 = rec(idx + 1, open_count)

                ans = op_1 or op_2 or op_3
            memo[(idx, open_count)] = ans
            
            return ans
        

        return rec(0,0)
```
