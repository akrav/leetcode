class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        left = 0
        steps_left = nums[0]
        while steps_left != 0 and left < len(nums)-1:
            steps_left -= 1
            left += 1
            steps_left = max(steps_left, nums[left])
        
        return True if left >= len(nums)-1 else False