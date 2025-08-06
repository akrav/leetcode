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