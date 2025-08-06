class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                    
                if (c == ')' and stack[-1] != '(') or \
                   (c == '}' and stack[-1] != '{') or \
                   (c == ']' and stack[-1] != '['):
                   return False
                else:
                    stack.pop()
        
        return stack == []
