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