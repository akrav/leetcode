[Back to Table of Contents](../../README.md)

# Binary Search
Difficulty: Easy

## Question
Binary Search
Solved 
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
O
(
l
o
g
n
)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.

## Solution Template
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # while left < right:
        #     mid = left + (right - left)//2

        #     if target <= nums[mid]:
        #         right = mid
        #     else:
        #         left = mid + 1
        

        while left < right:
            mid = left + math.ceil((right - left)/2)

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid
            
        
        return left if nums[left] == target else -1
```
