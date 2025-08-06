# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         l = 0
#         r = 0
#         total = 0
#         while r < len(nums):
#             total += nums[r]

#             if total >= k:
#                 if total == k:
#                     count += 1
#                 total -= nums[l]
#                 l += 1
#             r += 1
        
#         return count



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res