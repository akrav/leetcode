# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:

#         left = 0
#         right = len(nums) - 1

#         while left < right:
#             l = nums[left]
#             r = nums[right]
#             if l + r == target:
#                 return [left,right]
#             elif l + r < target:
#                 l += 1
#             else:
#                 r -= 1
#         return [-1,-1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(lambda: -1)

        for i in range(len(nums)):
            new_target = target - nums[i]
            if dic[new_target] != -1:
                return [dic[new_target], i]
            dic[nums[i]] = i
        return [-1,-1]