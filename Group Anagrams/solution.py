# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

#         def is_anagram(s, t):
#             s_dic = defaultdict(int)
#             t_dic = defaultdict(int)

#             if len(s) != len(t):
#                 return False

#             for i in range(len(s)):
#                 s_dic[s[i]] += 1
#                 t_dic[t[i]] += 1
            
#             for letter in s:
#                 if s_dic[letter] != t_dic[letter]:
#                     return False

#             return True
        
#         res = [[strs[0]]]
#         for i in range(1, len(strs)):
#             for group in res:
#                 # print(f"group: {group}, strs: {strs[i]}")
#                 if is_anagram(group[0], strs[i]):
#                     group.append(strs[i])
#                 else:
#                     res.append([strs[i]])
#                     i += 1

#         return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

        