class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        def xor(arr):
            result = 0
            for val in arr:
                result = result ^ val
            return result

        def combin(start, comb_arr):
            nonlocal res
            res += xor(comb_arr)

            for i in range(start, n):
                # if i > start and nums[i] == nums[i-1]:
                #     continue
                comb_arr.append(nums[i])
                combin(i+1, comb_arr)
                comb_arr.pop()
        
        combin(0, [])
        return res