class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()

        def rec_helper(start, path):

            self.res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                rec_helper(i+1, path)
                path.pop()
        
        rec_helper(0, [])
        return self.res

        