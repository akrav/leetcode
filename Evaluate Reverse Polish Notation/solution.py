class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                val_two = int(stack.pop())
                val_one = int(stack.pop())
                stack.append(val_one + val_two)
            elif c == "-":
                val_two = int(stack.pop())
                val_one = int(stack.pop())
                stack.append(val_one - val_two)
            elif c == "*":
                val_two = int(stack.pop())
                val_one = int(stack.pop())
                stack.append(val_one * val_two)
            elif c == "/":
                val_two = int(stack.pop())
                val_one = int(stack.pop())
                stack.append(val_one / val_two)
            else:
                stack.append(c)
        
        return int(stack[-1])
        