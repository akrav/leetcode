class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs_sum(start, path, target_points):
            if target_points < 0:
                return
            if target_points == 0:
                self.res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                # if i > start and nums[i] == nums[i-1]:
                #     continue
                
                path.append(nums[i])
                target_points -= nums[i]
                dfs_sum(i, path, target_points)
                path.pop()
                target_points += nums[i]
        
        dfs_sum(0, [], target)

        return self.res
        