[Back to Table of Contents](../README.md)

# Trapping Rain Water
Difficulty: Hard

## Question
Trapping Rain Water
Solved 
You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.

Example 1:



Input: height = [0,2,0,3,1,0,1,3,2,1]

Output: 9
Constraints:

1 <= height.length <= 1000
0 <= height[i] <= 1000

## Solution Template
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        max_l = 0
        max_r = len(height) - 1
        area = 0
# height=[0,1,0,2,1,0,1,3,2,1,2,1]
#        1
#    1   11 1
# _1_11_111111
        while left < right:
            print(f"left: {left}, max_l: {max_l}, height[left]: {height[left]}, height[max_l]: {height[max_l]}")
            print(f"right: {right}, max_r: {max_r}, height[right]: {height[right]}, height[max_r]: {height[max_r]}")
            print(f"area before: {area}")

            if height[left] >= height[max_l]:
                max_l = left
            else:
                area += (height[max_l] - height[left])

            
            if height[right] >= height[max_r]:
                max_r = right
            else:
                area += (height[max_r] - height[right])
            print(f"area after: {area}\n\n")

            if height[max_l] <= height[max_r]:
                left += 1
            else:
                right -= 1
        
        return area
            
```
