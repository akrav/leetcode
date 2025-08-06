class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0

        profit = 0

        while right < len(prices):
            pl = prices[left]
            pr = prices[right]

            profit = max(profit, (pr - pl))
            if pr < pl:
                left = right
            
            right += 1
        
        return profit