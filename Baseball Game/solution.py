class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                val = stack[-1]
                stack.append(2 * val)
            elif op == "+":
                val = stack[-1]
                val2 = stack[-2]
                stack.append(val+val2)
            else:
                stack.append(int(op))
        
        return 0 if len(stack) == 0 else sum(stack)