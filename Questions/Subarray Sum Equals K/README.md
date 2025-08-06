[Back to Table of Contents](../../README.md)

# Subarray Sum Equals K
Difficulty: Medium

## Question
Subarray Sum Equals K
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

## Solution Template
```python
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
```
