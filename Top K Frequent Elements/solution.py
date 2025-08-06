class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        res = []
        for key, value in sorted(dic.items(), key=lambda item: item[1], reverse=True):
            if len(res) == k:
                return res
            res.append(key)
        return res