class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.used = [False] * len(nums)

        def dfs_perm(path):
            if len(path) == len(nums):
                self.res.append(path[:])
                return
            
            for i in range(len(nums)):
                if self.used[i]:
                    continue
                
                # if i > 0 and nums[i] == nums[i-1] and not self.used[i-1]:
                #     continue
                    
                    
                self.used[i] = True
                path.append(nums[i])
                dfs_perm(path)
                self.used[i] = False
                path.pop()

        dfs_perm([])
        return self.res
        