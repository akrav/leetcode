[Back to Table of Contents](../README.md)

# Maximum Sum Circular Subarray
Difficulty: Medium

## Question
Maximum Sum Circular Subarray
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.
 

Constraints:

n == nums.length
1 <= n <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104

## Solution Template
```python
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
```
