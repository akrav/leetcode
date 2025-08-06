[Back to Table of Contents](../README.md)

# Generate Parentheses
Difficulty: Medium

## Question
Generate Parentheses
Solved 
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]
Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]
You may return the answer in any order.

Constraints:

1 <= n <= 7

## Solution Template
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def rec(c_stack, num, path):
            if num == 0 and c_stack==[]:
                ans.append(path)
                return
            
            if num > 0:
                path += "("
                c_stack.append(")")
                rec(c_stack, num-1, path)
                path = path[:-1]
                c_stack.pop()

            if c_stack != []:
                path += c_stack.pop()
                rec(c_stack, num, path)
                path = path[:-1]
                c_stack.append(")")
            
        
        rec([], n, "")
        return ans
```
