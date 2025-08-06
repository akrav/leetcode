# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         #find the first letter 
#         #find the last position of the first in the string
#         #check all letters in substring
#         #from right find first appearance of one of the letters in the substring
#         #and thats the substring
#         # remove substring found
#         # repeat until no letters are left in s
#         ans = []
#         while s != '':
#             left = 0
#             right = len(s)-1

#             while left < right and s[left] != s[right]:
#                 right -= 1
            
#             dic = {}
#             for i in range(left, right + 1):
#                 dic[s[i]] = True
            
#             left = 0
#             right = len(s)-1
            
#             print(dic)
#             while left < right and s[right] not in dic.keys():
#                 right -= 1
#             ans.append(right-left+1)
#             s = s[right+1:]
        
#         return ans
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = defaultdict(int)

        for i in range(len(s)):
            last_index[s[i]] = max(last_index[s[i]], i)
        
        print(last_index)
        
        count = 1
        curr = 0
        end = 0
        ans = []
        while curr < len(s):
            curr_letter = s[curr]
            end = max(end, last_index[curr_letter])
            if curr == end:
                ans.append(count)
                count = 0
            curr += 1
            count += 1 
        
        return ans
