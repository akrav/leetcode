class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()

        def dfs_sum(start, path, tar):
            if tar < 0:
                return
            if tar == 0:
                self.res.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                tar -= candidates[i]
                dfs_sum(i+1, path, tar)
                path.pop()
                tar += candidates[i]
        
        dfs_sum(0, [], target)
        return self.res