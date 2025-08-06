[Back to Table of Contents](../README.md)

# Contains Duplicate II
Difficulty: Easy

## Question
Contains Duplicate II
Solved
Easy
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105

## Solution Template
```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(lambda: -1)

        
        for i in range(len(nums)):
            val = nums[i]
            if dic[val] != -1:
                if (i - dic[val]) <= k:
                    return True
            dic[val] = i
        return False
```
