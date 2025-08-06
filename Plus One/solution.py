class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        next_power = [1]
        carry = 1
        for i in range(n-1,-1,-1):
            new_digit = digits[i] + carry

            remainder = new_digit % 10
            carry = new_digit // 10
            digits[i] = remainder
        
        if carry == 1:
            return next_power + digits
        return digits