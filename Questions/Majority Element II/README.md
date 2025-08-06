[Back to Table of Contents](../../README.md)

# Majority Element II
Difficulty: Medium

## Question
Majority Element II
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 

Follow up: Could you solve the problem in linear time and in O(1) space?

## Solution Template
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n // 3

        count_dic = defaultdict(int)
        nums_pointer = 0

        for i in range(len(nums)):
            num = nums[i]
            count_dic[num] += 1

            if count_dic[num] == target+1:
                nums[nums_pointer] = num
                nums_pointer += 1
        return nums[:nums_pointer]
        
```
