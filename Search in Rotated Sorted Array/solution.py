class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left)//2

            if nums[mid] > nums[left]:
                #[5,6,1,2*,3~,4]    mid = *, target = ~
                if nums[right] > nums[mid] and target > nums[mid] and target > nums[right]:
                    right = mid
                elif nums[right] > nums[mid] and target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                #[5,6,~1,2*,3,4]    mid = *, target = ~
                elif nums[right] > nums[mid] and target <= nums[mid]:
                    right = mid
                #[3,4,5*,6,1~,2]
                elif nums[right] <= nums[mid] and target < nums[mid] and target > nums[right]:
                    right = mid
                #[3,4~,5*,6,1,2]
                elif nums[right] <= nums[mid] and target < nums[mid] and target <= nums[right]:
                    left = mid + 1
                elif nums[right] <= nums[mid] and target >= nums[mid] and target > nums[right]:
                    left = mid + 1
            
            else:

                #[5,6,1,2*,3~,4]    mid = *, target = ~
                if nums[right] > nums[mid] and target > nums[mid] and target > nums[right]:
                    right = mid
                elif nums[right] > nums[mid] and target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                #[5,6,~1,2*,3,4]    mid = *, target = ~
                elif nums[right] > nums[mid] and target <= nums[mid]:
                    right = mid
                #[3,4,5*,6,1~,2]
                elif nums[right] <= nums[mid] and target < nums[mid] and target > nums[right]:
                    right = mid
                #[3,4~,5*,6,1,2]
                elif nums[right] <= nums[mid] and target < nums[mid] and target <= nums[right]:
                    left = mid + 1
                elif nums[right] <= nums[mid] and target >= nums[mid] and target > nums[right]:
                    right = mid

        return left if nums[left] == target else -1