class Solution:
    def numSquares(self, n: int) -> int:
        sqrt_n = math.floor(n ** (1/2))
        min_count = 100000

        def rec(end, target, count):
            nonlocal min_count
            if target == 0:
                min_count = min(min_count, count)
                return 
            if target < 0:
                return 
            if count >= min_count:
                return
            
            for i in range(end, 0, -1):
                rec(i, target - i**2, count + 1)

            return 
        rec(sqrt_n, n, 0)
        return min_count