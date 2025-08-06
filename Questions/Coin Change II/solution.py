class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def rec(total, start):
            if total < 0:
                return 0
            if total == 0:
                return 1
            if f"{total},{start}" in memo:
                return memo[f"{total},{start}"]
            
            count = 0
            for i in range(start, len(coins)):
                count += rec(total - coins[i], i)
            
            memo[f"{total},{start}"] = count
            
            return count
        
        return rec(amount, 0)
        