[Back to Table of Contents](../README.md)

# Maximum Subarray
Difficulty: Medium

## Question
Maximum Subarray
Solved 
Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-3,4,-2,2,1,-1,4]

Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Example 2:

Input: nums = [-1]

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

## Solution Template
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        right = 1

        max_seen = nums[0]
        ans = max(nums[0], 0)
        while right < len(nums):
            ans = max(ans+nums[right], nums[right])
            max_seen = max(max_seen, ans)
            right += 1
        
        return max_seen

[-2,1,-3,4,-1,2,1,-5,4]
[ 0,1,-2,4, 3,5,6, 1, 5]
```
