class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        used = [False] * n

        def perm(perm_arr):
            print(f"perm_arr: {perm_arr}")
            if len(perm_arr) == n:
                result.append(perm_arr[:])
                return
            
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and used[i - 1] == True:
                    continue
                
                perm_arr.append(nums[i])
                used[i] = True
                perm(perm_arr)
                perm_arr.pop()
                used[i] = False
        
        perm([])
        return result
        