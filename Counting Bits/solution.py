class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            count = 0
            m = i
            while m != 0:
                count += m%2
                m = m >> 1
            res.append(count)
        return res
            