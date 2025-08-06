[Back to Table of Contents](../README.md)

# Find Minimum in Rotated Sorted Array
Difficulty: Medium

## Question
Find Minimum in Rotated Sorted Array
Solved 
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Notice that rotating the array 4 times moves the last four elements of the array to the beginning. Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2]

Output: 1
Example 2:

Input: nums = [4,5,0,1,2,3]

Output: 0
Example 3:

Input: nums = [4,5,6,7]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

## Solution Template
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left)//2

            if nums[mid] > nums[left]:
                # regular array find left
                # [1,2,3,4*,5,6]
                if nums[right] >= nums[mid]:
                    right = mid

                # else smallest value is on right of mid
                # so move left up
                # [2,3,4,5*,6,1]
                else: 
                    left = mid + 1
            
            else:
                # [6,1,2,3*,4,5]
                # want to decrease and move left so we decrease right
                if nums[right] >= nums[mid]:
                    right = mid

                # [3,4,5,6*,1,2]
                # want to increase and move right so we increase left
                else: 
                    left = mid + 1
        
        return nums[right]

        
```
