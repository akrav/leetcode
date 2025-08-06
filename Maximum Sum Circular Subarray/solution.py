class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #find min window
        min_window = nums[0]
        global_min = nums[0]
        for num in nums[1:]:
            min_window = min(num, min_window + num)
            global_min = min(global_min, min_window)

        #find max window
        max_window = nums[0]
        global_max = nums[0]
        for num in nums[1:]:
            max_window = max(num, max_window + num)
            global_max = max(global_max, max_window)

        #total window
        total_window = sum(nums)

        if global_max < 0:
            return global_max
        #total window - min window can be a possible max window option, but we need to compare

        return max(global_max, (total_window - global_min))