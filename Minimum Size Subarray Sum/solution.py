class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        n = len(nums)
        total = nums[0]
        min_len = 10000000
        while right < n:
            print(f"right: {right}, total: {total}")

            if total < target:
                right += 1
                if right < n:
                    total += nums[right]
            else:
                min_len = min(min_len, (right-left + 1))
                total -= nums[left]
                left += 1
            
        return 0 if min_len == 10000000 else min_len