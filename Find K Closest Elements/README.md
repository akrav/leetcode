[Back to Table of Contents](../README.md)

# Find K Closest Elements
Difficulty: Medium

## Question
Find K Closest Elements
Solved
Medium
Topics
premium lock icon
Companies
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104

## Solution Template
```python
# import heapq as hq
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         pq = []


#         for i in range(len(arr)):
#             if len(pq) < k:
#                 hq.heappush(pq, (-1 * abs(x - arr[i]),arr[i]))
#             else:
#                 difference, val = pq[0]
#                 if difference < (-1 * abs(x - arr[i])):
#                     hq.heappop(pq)
#                     hq.heappush(pq, (-1 * abs(x - arr[i]),arr[i]))
#         res = []
#         while pq:
#             res.append(hq.heappop(pq)[1])
#         res.sort()
#         return res

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        
        return arr[l: r + 1]
```
