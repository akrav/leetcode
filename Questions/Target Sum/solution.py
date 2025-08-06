class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def rec(idx, val):
            if idx == len(nums):
                if val == 0:
                    return 1
                return 0

            add_op = rec(idx + 1, val + nums[idx])
            sub_op = rec(idx + 1, val - nums[idx])

            return add_op + sub_op
        
        return rec(0, target)