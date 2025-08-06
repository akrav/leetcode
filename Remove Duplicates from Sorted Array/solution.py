class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert_pointer = 0

        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue
            nums[insert_pointer] = nums[i]
            insert_pointer += 1
        
        return insert_pointer
        