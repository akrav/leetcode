class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):    
            res += i+1 - nums[i]
        return res

[0,2]