[Back to Table of Contents](../../README.md)

# Permutations II
Difficulty: Medium

## Question
Permutations II
Solved
Medium
Topics
premium lock icon
Companies
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

## Solution Template
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        used = [False] * n

        def perm(perm_arr):
            print(f"perm_arr: {perm_arr}")
            if len(perm_arr) == n:
                result.append(perm_arr[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i - 1] == True:
                    continue
                
                perm_arr.append(nums[i])
                used[i] = True
                perm(perm_arr)
                perm_arr.pop()
                used[i] = False
        
        perm([])
        return result
        
```
