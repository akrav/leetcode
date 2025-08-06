[Back to Table of Contents](../../README.md)

# Longest Consecutive Sequence
Difficulty: Medium

## Question
Longest Consecutive Sequence
Solved 
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

## Solution Template
```python
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         dic = defaultdict(int)

#         for i in range(len(nums)):
#             val = nums[i]
#             if nums[i] - 1  in dic.keys():
#                 dic[nums[i]] = max (dic[nums[i]], dic[nums[i] - 1]+1)
#             else:
#                 dic[nums[i]] = 1
#         return max(dic.values())
import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dic = defaultdict(int)
        
        keys_list = []
        for i in range(len(nums)):
            val = nums[i]
            dic[val] = 1
            heapq.heappush(keys_list, val)
        
        for i in range(len(keys_list)):
            key = heapq.heappop(keys_list)
            dic[key] = max(dic[key], dic[key-1]+1)
        
        return max(dic.values())
            
```
