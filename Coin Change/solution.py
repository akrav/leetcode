class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.min_amount = 1000000
        coins.reverse()
        memo = {}

        def rec(total, count):
            if total < 0:
                return 
            if count >= self.min_amount:
                return
            if total in memo and count >= memo[total]:
                return memo[total]
            if total == 0:
                self.min_amount = min(self.min_amount, count)
                return 

            
            for coin in coins:
                rec(total - coin, count + 1)

            if total not in memo:
                memo[total] = count
            else:
                memo[total] = min(memo[total], count)

            return
        
        rec(amount, 0)
        return -1 if self.min_amount == 1000000 else self.min_amount
            