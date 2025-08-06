# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_dic = defaultdict(int)

#         for letter in s:
#             s_dic[letter] += 1
        
#         for letter in t:
#             s_dic[letter] -= 1
#             if s_dic[letter] < 0:
#                 return False
        
#         for letter in s:
#             if s_dic[letter] != 0:
#                 return False
#         return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_dic[s[i]] += 1
            t_dic[t[i]] += 1
        
        for letter in s:
            if s_dic[letter] != t_dic[letter]:
                return False
        return True
        