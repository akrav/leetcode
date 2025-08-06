class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0
        
        min_value = 0
        total = 0
        for i in range(1,n):
            profit = prices[i] - prices[i-1]

            if profit >= 0:
                total += profit

        return total