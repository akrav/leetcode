[Back to Table of Contents](../../README.md)

# Container With Most Water
Difficulty: Medium

## Question
Container With Most Water
Solved 
You are given an integer array heights where heights[i] represents the height of the 
i
t
h
i 
th
  bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:



Input: height = [1,7,2,5,4,7,3,6]

Output: 36
Example 2:

Input: height = [2,2,2]

Output: 4
Constraints:

2 <= height.length <= 1000
0 <= height[i] <= 1000

## Solution Template
```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        area = 0
        while left < right:
            lh = heights[left]
            rh = heights[right]
            area = max(area, min(lh, rh) * (right-left))

            if lh <= rh:
                left += 1
            else:
                right -= 1
        
        return area
```
