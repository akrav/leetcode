class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            # get first number & with 1 to get the bit at the last position
            # ex 5 101  we want to check what the last 1 is
            # 1 & 1 is 1
            # move value to the end of the bit ar idx 31 below and continue
            res += (bit << (31 - i))
        return res