class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1
            if dic[num] > 1:
                return True
        return False