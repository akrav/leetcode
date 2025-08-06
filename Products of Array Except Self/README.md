[Back to Table of Contents](../README.md)

# Products of Array Except Self
Difficulty: Medium

## Question
Products of Array Except Self
Solved 
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20

## Solution Template
```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        fowards = [nums[0]]
        backwards = [nums[-1]]

        for i in range(1, len(nums)):
            fowards.append(fowards[i-1] * nums[i])
        j = 0 
        for i in range(len(nums)-2, -1, -1 ):
            backwards.append(backwards[j] * nums[i])
            j+=1
        backwards = backwards[::-1]

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(backwards[i+1])
            elif i == len(nums) - 1:
                ans.append(fowards[i-1])
            else:
                ans.append(fowards[i-1] * backwards[i+1])
        return ans
```
