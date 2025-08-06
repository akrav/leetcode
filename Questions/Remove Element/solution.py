class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_spot = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[last_spot] = nums[i]
            last_spot += 1
        return last_spot
            