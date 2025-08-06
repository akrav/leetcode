[Back to Table of Contents](../../README.md)

# Permutations
Difficulty: Medium

## Question
Permutations
Solved 
Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]

Output: [[7]]
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10

## Solution Template
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.used = [False] * len(nums)

        def dfs_perm(path):
            if len(path) == len(nums):
                self.res.append(path[:])
                return
            
            for i in range(len(nums)):
                if self.used[i]:
                    continue
                
                # if i > 0 and nums[i] == nums[i-1] and not self.used[i-1]:
                #     continue
                    
                    
                self.used[i] = True
                path.append(nums[i])
                dfs_perm(path)
                self.used[i] = False
                path.pop()

        dfs_perm([])
        return self.res
        
```
