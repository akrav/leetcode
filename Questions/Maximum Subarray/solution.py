class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        right = 1

        max_seen = nums[0]
        ans = max(nums[0], 0)
        while right < len(nums):
            ans = max(ans+nums[right], nums[right])
            max_seen = max(max_seen, ans)
            right += 1
        
        return max_seen

[-2,1,-3,4,-1,2,1,-5,4]
[ 0,1,-2,4, 3,5,6, 1, 5]