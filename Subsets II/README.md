[Back to Table of Contents](../README.md)

# Subsets II
Difficulty: Medium

## Question
Subsets II
Solved 
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]
Constraints:

1 <= nums.length <= 11
-20 <= nums[i] <= 20

## Solution Template
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.used = [False] * len(nums)
        nums.sort()

        def dfs_sub(start, path):
            self.res.append(path[:])
            if len(path) > len(nums):
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                dfs_sub(i+1, path)
                path.pop()
        
        dfs_sub(0,[])
        return self.res
```
