# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         t_dic = defaultdict(int)
#         s_dic = defaultdict(int)
        
#         def compare(tcom, scom):
#             for letter in t:
#                 if t_dic[letter] > s_dic[letter]:
#                     return False
#             return True
        
#         for letter in t:
#             t_dic[letter] += 1
#         left = 0
#         res = ''
#         min_res = ''
#         for right in range(len(s)):
#             res += s[right]
#             s_dic[s[right]] += 1
            
#             comp_res = compare(t_dic, s_dic)
#             while compare(t_dic, s_dic):
#                 if min_res == '':
#                     min_res = res
#                 elif min_res != '' and len(res) < len(min_res):
#                     min_res = res
                
#                 s_dic[s[left]] -= 1
#                 res = res[1:]
#                 left += 1

#         return min_res


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dic = defaultdict(int)
        s_dic = defaultdict(int)
        
        def compare(tcom, scom):
            for letter in t:
                if t_dic[letter] > s_dic[letter]:
                    return False
            return True
        
        for letter in t:
            t_dic[letter] += 1
        need = len(t_dic)
        left = 0
        res = ''
        min_res = ''
        have = 0
        for right in range(len(s)):
            res += s[right]
            s_dic[s[right]] += 1
            if s_dic[s[right]] == t_dic[s[right]]:
                have += 1
            
            
            while have == need:
                print(f"have: {have}, need: {need}, res: {res}")
                if min_res == '':
                    min_res = res
                elif min_res != '' and len(res) < len(min_res):
                    min_res = res
                
                
                if s[left] in t_dic.keys():
                    if s_dic[s[left]] == t_dic[s[left]]:
                        have -= 1
                        
                s_dic[s[left]] -= 1
                res = res[1:]
                left += 1

        return min_res
                    
                    
                    
                    