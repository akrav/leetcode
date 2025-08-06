# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         dic = defaultdict(int)

#         for i in range(len(nums)):
#             val = nums[i]
#             if nums[i] - 1  in dic.keys():
#                 dic[nums[i]] = max (dic[nums[i]], dic[nums[i] - 1]+1)
#             else:
#                 dic[nums[i]] = 1
#         return max(dic.values())
import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dic = defaultdict(int)
        
        keys_list = []
        for i in range(len(nums)):
            val = nums[i]
            dic[val] = 1
            heapq.heappush(keys_list, val)
        
        for i in range(len(keys_list)):
            key = heapq.heappop(keys_list)
            dic[key] = max(dic[key], dic[key-1]+1)
        
        return max(dic.values())
            