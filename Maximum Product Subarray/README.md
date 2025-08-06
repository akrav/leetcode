[Back to Table of Contents](../README.md)

# Maximum Product Subarray
Difficulty: Medium

## Question
Maximum Product Subarray
Solved 
Given an integer array nums, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Example 1:

Input: nums = [1,2,-3,4]

Output: 4
Example 2:

Input: nums = [-2,-1]

Output: 2
Constraints:

1 <= nums.length <= 1000
-10 <= nums[i] <= 10

## Solution Template
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1

        total_max = -10000000
        for num in nums:
            if num == 0:
                cur_min = 1
                cur_max = 1
            
            new_val_one = cur_max * num
            new_val_two = cur_min * num
            cur_min = min(new_val_one, new_val_two, num)
            cur_max = max(new_val_one, new_val_two, num)

            total_max = max(total_max, cur_max)

        return total_max
```
