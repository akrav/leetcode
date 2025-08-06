class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left)//2

            if nums[mid] > nums[left]:
                # regular array find left
                # [1,2,3,4*,5,6]
                if nums[right] >= nums[mid]:
                    right = mid

                # else smallest value is on right of mid
                # so move left up
                # [2,3,4,5*,6,1]
                else: 
                    left = mid + 1
            
            else:
                # [6,1,2,3*,4,5]
                # want to decrease and move left so we decrease right
                if nums[right] >= nums[mid]:
                    right = mid

                # [3,4,5,6*,1,2]
                # want to increase and move right so we increase left
                else: 
                    left = mid + 1
        
        return nums[right]

        