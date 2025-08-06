[Back to Table of Contents](../../README.md)

# Sort Colors
Difficulty: Medium

## Question
Sort Colors
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

## Solution Template
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def merge_sort(arr, l, r):
            
            if l >= r:
                return
            
            
            m = l + (r - l)//2
            merge_sort(arr, l, m)
            merge_sort(arr, m+1, r)

            arr_pointer = l
            list1 = arr[l:m+1]
            list2 = arr[m+1:r+1]
            l1_pointer = 0
            l2_pointer = 0

            while l1_pointer < len(list1) and l2_pointer < len(list2):

                if list1[l1_pointer] <= list2[l2_pointer]:
                    arr[arr_pointer] = list1[l1_pointer]
                    l1_pointer += 1
                else:
                    arr[arr_pointer] = list2[l2_pointer]
                    l2_pointer += 1
                arr_pointer += 1
            

            while l1_pointer < len(list1):
                arr[arr_pointer] = list1[l1_pointer]
                l1_pointer += 1
                arr_pointer += 1
            
            while l2_pointer < len(list2):
                arr[arr_pointer] = list2[l2_pointer]
                l2_pointer += 1
                arr_pointer += 1
            
            
            return
        
        merge_sort(nums, 0, len(nums)-1)


        
```
