[Back to Table of Contents](../README.md)

# Find the Duplicate Number
Difficulty: Medium

## Question
Find the Duplicate Number
Solved 
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Example 1:

Input: nums = [1,2,3,2,2]

Output: 2
Example 2:

Input: nums = [1,2,3,4,4]

Output: 4
Follow-up: Can you solve the problem without modifying the array nums and using 
O
(
1
)
O(1) extra space?

Constraints:

1 <= n <= 10000
nums.length == n + 1
1 <= nums[i] <= n

## Solution Template
```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use numbers in list to go to index
        # use fast and slow pointers concept
        # when fast and slow meet they are on the index
        # value that repeats

        slow = nums[0]
        fast = nums[0]

        slow = nums[slow]
        fast = nums[nums[fast]]

        looped = False
        while slow != fast:
            if looped == False:
                slow = nums[slow]
                fast = nums[nums[fast]]
            else:
                slow = nums[slow]
                fast = nums[fast]

            if slow == fast and looped == False:
                slow = nums[0]
                looped = True

        
        return slow
```
