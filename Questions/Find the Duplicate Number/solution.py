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