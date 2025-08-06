class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 1:
            if nums[0] == target:
                return True
            else: False

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right - left)//2
            mid_val = nums[mid]

            if mid_val == target:
                return True

            if nums[left] < nums[mid]:  # Left portion
                if nums[left] <= target and target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:  # Right portion
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                left += 1        
        return False
        