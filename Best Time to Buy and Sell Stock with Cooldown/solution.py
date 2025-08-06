class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.n = len(prices)
        
        def rec(idx, have_coin):
            if idx >= self.n:
                return 0
            
            # options
            # buy or skip
            if have_coin == False:
                #buy
                option_1 = rec(idx + 1, True) - prices[idx]
                #skip
                option_2 = rec(idx + 1, False)
             
            else:
                # sell
                option_1 = rec(idx + 2, False) + prices[idx]
                #skip
                option_2 = rec(idx + 1, True)
            
            return max(option_1, option_2)
        
        return rec(0, False)
                
           
            