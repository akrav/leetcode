[Back to Table of Contents](../../README.md)

# Longest Increasing Subsequence
Difficulty: Medium

## Question
Longest Increasing Subsequence
Solved 
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
Example 1:

Input: nums = [9,1,4,2,3,3,7]

Output: 4
Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

Example 2:

Input: nums = [0,3,1,3,2,3]

Output: 4
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000

## Solution Template
```python
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         self.res = []

#         def rec(idx, path):
#             if idx == len(nums):
#                 self.res.append(path[:])
#                 return

#             if path == []:
#                 path.append(nums[idx])
#                 rec(idx + 1, path)
#                 path.pop()
#                 rec(idx + 1, path)
#             else:
#                 last_taken = path[-1]

#                 if nums[idx] > last_taken:
#                     path.append(nums[idx])
#                     rec(idx + 1, path)
#                     path.pop()
#                 rec(idx + 1, path)
            
#             return
#         rec(0, [])
#         max_length = 0

#         for ans in self.res:
#             max_length = max(max_length, len(ans))

#         return max_length


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        self.res = []

        def rec(idx, last_taken_idx):
            if idx == len(nums):
                return 0
            taken = 0
            not_taken = 0
            if last_taken_idx == -1:
                taken = rec(idx + 1, idx) + 1
                not_taken = rec(idx + 1, last_taken_idx)
            else:
                if nums[idx] > nums[last_taken_idx]:
                    taken = rec(idx + 1, idx) + 1
                not_taken = rec(idx + 1, last_taken_idx)
            
            return max(taken, not_taken)
        

        return rec(0, -1)
```
