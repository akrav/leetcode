class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        total_sum = sum(nums)
        half_sum = total_sum//2

        if total_sum % 2 == 1:
            return False
        
        def rec(val, start):
            if val < 0:
                return False
            if val == 0:
                return True
            if val in memo and memo[val]:
                return memo[val]
            
            overall = False

            for i in range(start,len(nums)):
                overall = overall or rec(val-nums[i], i+1)
            memo[val] = overall
            return overall
        
        return rec(half_sum, 0)


        