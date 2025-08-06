[Back to Table of Contents](../../README.md)

# Partition to K Equal Sum Subsets
Difficulty: Medium

## Question
Partition to K Equal Sum Subsets
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].

## Solution Template
```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        n = len(nums)
        nums.sort(reverse=True)
        if total % k != 0:
            return False
        
        side_len = total / k
        
        subsets = [side_len] * k

        def rec(idx):
            if idx == n:
                return True
            
            for i in range(k):
                if subsets[i] - nums[idx] >= 0:
                    subsets[i] -= nums[idx]
                    found_solution = rec(idx+1)
                    if found_solution:
                        return True
                    subsets[i] += nums[idx]

                    if subsets[i] == side_len:
                        break
            return False

        return rec(0)

# class Solution:
#     def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#         total = sum(nums)
#         n = len(nums)
#         nums.sort(reverse=True)  
#         if total % k != 0:
#             return False

#         target = total // k
#         # "subsets[i]" will track how much capacity is left in the i-th subset
#         subsets = [target] * k

#         # Memo to avoid repeating states:
#         # Key will be (idx, tuple(sorted_subsets))
#         #   - "idx" is which element in nums we are trying to place
#         #   - "sorted_subsets" is the sorted version of 'subsets' 
#         #     so that different permutations of the same leftover capacities
#         #     look identical in the memo
#         memo = {}

#         def backtrack(idx):
#             # If we've assigned all numbers successfully, we're done
#             if idx == n:
#                 return True

#             # Create a memo key by sorting 'subsets'
#             # Sorting ensures that e.g. [2,1,2] and [2,2,1] 
#             # are recognized as the same leftover capacities
#             key = (idx, tuple(sorted(subsets)))
#             if key in memo:
#                 return memo[key]

#             for i in range(k):
#                 # If current nums[idx] can fit in subsets[i]
#                 if subsets[i] >= nums[idx]:
#                     # Place nums[idx] in subset i
#                     subsets[i] -= nums[idx]

#                     if backtrack(idx + 1):
#                         memo[key] = True
#                         return True

#                     # Backtrack (remove nums[idx] from subset i)
#                     subsets[i] += nums[idx]

#                 # Optimization: if subsets[i] was exactly target before we tried to place nums[idx],
#                 # and we put it back to target, then no need to try the next empty bucket 
#                 # (this helps prune symmetrical states)
#                 if subsets[i] == target:
#                     break

#             memo[key] = False
#             return False

#         return backtrack(0)
```
