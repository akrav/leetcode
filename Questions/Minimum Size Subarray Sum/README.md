[Back to Table of Contents](../../README.md)

# Minimum Size Subarray Sum
Difficulty: Medium

## Question
Minimum Size Subarray Sum
Solved
Medium
Topics
premium lock icon
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).

## Solution Template
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)
        total = nums[0]
        min_len = 10000000
        while right < n:
            print(f"right: {right}, total: {total}")

            if total < target:
                right += 1
                if right < n:
                    total += nums[right]
            else:
                min_len = min(min_len, (right-left + 1))
                total -= nums[left]
                left += 1
            
        return 0 if min_len == 10000000 else min_len
```
