[Back to Table of Contents](../../README.md)

# House Robber II
Difficulty: Medium

## Question
House Robber II
Solved 
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [3,4,3]

Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

## Solution Template
```python
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         t = len(nums)
#         if t == 1:
#             return nums[0]
#         if t == 2:
#             return max(nums[0], nums[1])

#         self.memo = {}


#         def rec(start, end):
#             if end < start:
#                 return 0
#             if end == start:
#                 return nums[start]
#             if end in self.memo:
#                 return self.memo[end]
            
#             op_one = rec(start, end - 1)
#             op_two = rec(start, end - 2)

#             self.memo[end] = max(op_two + nums[end], op_one)

#             return self.memo[end]
        
#         one = rec(0, t-2)
#         self.memo = {}
#         two = rec(1, t-1)
        
#         return max(one, two)


class Solution:
    def rob(self, nums: List[int]) -> int:
        t = len(nums)
        if t == 1:
            return nums[0]
        if t == 2:
            return max(nums[0], nums[1])
            
        prev_one = nums[0]
        curr_one = max(nums[0], nums[1])
        count_one = 0

        for i in range(2,t-1):
            count_one = max(prev_one + nums[i], curr_one)
            prev_one = curr_one
            curr_one = count_one
        
        ans_one = max(curr_one, prev_one)

        prev_two = nums[1]
        curr_two = max(nums[2], nums[1])
        count_two = 0
        for i in range(3, t):
            count_two = max(prev_two + nums[i], curr_two)
            prev_two = curr_two
            curr_two = count_two
        
        ans_two = max(curr_two, prev_two)

        return max(ans_one, ans_two)
```
