[Back to Table of Contents](../README.md)

# Partition Equal Subset Sum
Difficulty: Medium

## Question
Partition Equal Subset Sum
Solved 
You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]

Output: true
Explanation: The array can be partitioned as [1, 4] and [2, 3].

Example 2:

Input: nums = [1,2,3,4,5]

Output: false
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 50

## Solution Template
```python
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


        
```
