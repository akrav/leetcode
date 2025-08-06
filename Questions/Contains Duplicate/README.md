[Back to Table of Contents](../../README.md)

# Contains Duplicate
Difficulty: Easy

## Question
Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

## Solution Template
```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1
            if dic[num] > 1:
                return True
        return False
```
