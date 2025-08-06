[Back to Table of Contents](../README.md)

# Longest Turbulent Subarray
Difficulty: Medium

## Question
Longest Turbulent Subarray
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
Example 2:

Input: arr = [4,8,12,16]
Output: 2
Example 3:

Input: arr = [100]
Output: 1
 

Constraints:

1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109

## Solution Template
```python
# class Solution:
#     def maxTurbulenceSize(self, arr: List[int]) -> int:
#         if len(arr) == 1:
#             return 1

#         for i in range(len(arr)-1):
#             arr[i] = arr[i+1] - arr[i]
        
#         max_count = 1 if sum(arr[:-1]) != 0 else 0
#         count = 1
#         for i in range(len(arr)-2):
            
#             if arr[i] == 0 or arr[i+1] == 0:
#                 count = 1
#                 continue

#             if arr[i]/abs(arr[i]) != arr[i+1]/abs(arr[i+1]):
#                 count += 1
#             else:
#                 count = 1
            
#             max_count = max(max_count, count)
#         return 1 if max_count == 0 else max_count + 1


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r, res, prev = 0, 1, 1, ""

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        return res
```
