class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        fowards = [nums[0]]
        backwards = [nums[-1]]

        for i in range(1, len(nums)):
            fowards.append(fowards[i-1] * nums[i])
        j = 0 
        for i in range(len(nums)-2, -1, -1 ):
            backwards.append(backwards[j] * nums[i])
            j+=1
        backwards = backwards[::-1]

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(backwards[i+1])
            elif i == len(nums) - 1:
                ans.append(fowards[i-1])
            else:
                ans.append(fowards[i-1] * backwards[i+1])
        return ans