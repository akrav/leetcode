class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(lambda: -1)

        
        for i in range(len(nums)):
            val = nums[i]
            if dic[val] != -1:
                if (i - dic[val]) <= k:
                    return True
            dic[val] = i
        return False