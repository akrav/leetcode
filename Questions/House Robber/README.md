[Back to Table of Contents](../../README.md)

# House Robber
Difficulty: Medium

## Question
House Robber
Solved 
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [1,1,3,3]

Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

## Solution Template
```python
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         self.memo = {}
        
#         def rec(n):
#             if n < 0:
#                 return 0
#             if n == 0:
#                 return nums[0]

#             if n in self.memo:
#                 return self.memo[n]
            
#             op_one = rec(n - 1)
#             op_two = rec(n - 2)

#             self.memo[n] = max(op_one, op_two + nums[n])

#             return self.memo[n]
        
#         return rec(len(nums) - 1)



class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        
        prev = nums[0]
        curr = max(nums[0],nums[1])

        print(f"prev: {prev}, curr: {curr}")
        for i in range(2, n):
            count = max(prev + nums[i], curr)
            prev = curr
            curr = count
            print(f"prev: {prev}, curr: {curr}")

        return count
```
