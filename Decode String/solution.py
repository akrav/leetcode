class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        for i in range(len(s)):
            if s[i] == "]":
                concat_str = ''
                while stack and stack[-1] != '[':
                    concat_str = stack.pop() + concat_str
                print(concat_str)
                if stack and stack[-1] == '[':
                    stack.pop()
                    get_multiplier = ''
                    while stack and stack[-1] in ['0','1','2','3','4','5','6','7','8','9']:
                        get_multiplier = stack.pop() + get_multiplier
                    
                    stack.append(int(get_multiplier) * concat_str)
            else:
                stack.append(s[i])
            
        return "".join(stack)