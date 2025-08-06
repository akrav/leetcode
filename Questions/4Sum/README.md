[Back to Table of Contents](../../README.md)

# 4Sum
Difficulty: Medium

## Question
4Sum
Solved
Medium
Topics
premium lock icon
Companies
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

## Solution Template
```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = set([])

        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n-1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                         res.add((nums[i], nums[j], nums[left], nums[right]))
                         left += 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        ans = []
        for p in res:
            ans.append(list(p))
        return ans
        
```
