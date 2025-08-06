[Back to Table of Contents](../../README.md)

# Subsets
Difficulty: Medium

## Question
Subsets
Solved 
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [7]

Output: [[],[7]]
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

## Solution Template
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()

        def rec_helper(start, path):

            self.res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                rec_helper(i+1, path)
                path.pop()
        
        rec_helper(0, [])
        return self.res

        
```
