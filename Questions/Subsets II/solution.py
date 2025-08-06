class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.used = [False] * len(nums)
        nums.sort()

        def dfs_sub(start, path):
            self.res.append(path[:])
            if len(path) > len(nums):
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                dfs_sub(i+1, path)
                path.pop()
        
        dfs_sub(0,[])
        return self.res