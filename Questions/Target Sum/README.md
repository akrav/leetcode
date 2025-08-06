[Back to Table of Contents](../../README.md)

# Target Sum
Difficulty: Medium

## Question
Target Sum
Solved 
You are given an array of integers nums and an integer target.

For each number in the array, you can choose to either add or subtract it to a total sum.

For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the expression such that the total sum equals target.

Example 1:

Input: nums = [2,2,2], target = 2

Output: 3
Explanation: There are 3 different ways to sum the input numbers to get a sum of 2.
+2 +2 -2 = 2
+2 -2 +2 = 2
-2 +2 +2 = 2

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
-1000 <= target <= 1000

## Solution Template
```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def rec(idx, val):
            if idx == len(nums):
                if val == 0:
                    return 1
                return 0

            add_op = rec(idx + 1, val + nums[idx])
            sub_op = rec(idx + 1, val - nums[idx])

            return add_op + sub_op
        
        return rec(0, target)
```
