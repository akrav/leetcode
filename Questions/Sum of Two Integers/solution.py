class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            c  = (a ^ b) & mask
            b = ((a & b) << 1) & mask
            a = c
        
        return a if a <= max_int else ~(a ^ mask)
        