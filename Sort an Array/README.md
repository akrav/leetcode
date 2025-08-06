[Back to Table of Contents](../README.md)

# Sort an Array
Difficulty: Medium

## Question
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104

## Solution Template
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(list1, list2):
            if len(list1) == 1 and len(list2) == 0:
                return list1
            if len(list1) == 0 and len(list2) == 1:
                return list2
            if len(list1) == 1 and len(list2) == 1:
                if list1[0] < list2[0]:
                    return list1 + list2
                return list2 + list1
            
            list1_mid = len(list1)//2
            list2_mid = len(list2)//2

            sorted_list1 = merge_sort(list1[:list1_mid], list1[list1_mid:])
            sorted_list2 = merge_sort(list2[:list2_mid], list2[list2_mid:])


            p_l1 = 0
            p_l2 = 0
            sort_full_list = []
            while p_l1 < len(sorted_list1) and p_l2 < len(sorted_list2):

                if sorted_list1[p_l1] < sorted_list2[p_l2]:
                    sort_full_list.append(sorted_list1[p_l1])
                    p_l1 += 1
                else:
                     sort_full_list.append(sorted_list2[p_l2])
                     p_l2 += 1
            
            
            
            if p_l1 < len(list1):
                sort_full_list = sort_full_list + sorted_list1[p_l1:]
            if p_l2 < len(list2):
                sort_full_list = sort_full_list + sorted_list2[p_l2:]

            return sort_full_list
        
        return merge_sort(nums[:len(nums)//2], nums[len(nums)//2:])
        
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def merge(arr, L, M, R):
#             left, right = arr[L : M + 1], arr[M + 1 : R + 1]
#             i, j, k = L, 0, 0

#             while j < len(left) and k < len(right):
#                 if left[j] <= right[k]:
#                     arr[i] = left[j]
#                     j += 1
#                 else:
#                     arr[i] = right[k]
#                     k += 1
#                 i += 1
#             while j < len(left):
#                 nums[i] = left[j]
#                 j += 1
#                 i += 1
#             while k < len(right):
#                 nums[i] = right[k]
#                 k += 1
#                 i += 1
        
#         def mergeSort(arr, l, r):
#             if l == r:
#                 return

#             m = (l + r) // 2
#             mergeSort(arr, l, m)
#             mergeSort(arr, m + 1, r)
#             merge(arr, l, m, r)
#             return
        
#         mergeSort(nums, 0, len(nums))
#         return nums
```
