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