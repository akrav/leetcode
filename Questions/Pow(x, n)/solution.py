class Solution:
    def myPow(self, x: float, n: int) -> float:
        num = 1
        is_positive = n >= 0

        for i in range(abs(n)):
            if is_positive:
                num *= x
            else:
                num /= x
        return num
        