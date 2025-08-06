class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def rec(start, target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if (start, target) in memo:
                return memo[(start, target)] 
            
            count = 0
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                count += rec(i, target-nums[i])
            
            memo[(start, target)] = count
            
            return memo[(start, target)]
        c = rec(0, target)
        return c
        