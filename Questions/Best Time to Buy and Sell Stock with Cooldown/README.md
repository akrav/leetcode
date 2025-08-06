[Back to Table of Contents](../../README.md)

# Best Time to Buy and Sell Stock with Cooldown
Difficulty: Medium

## Question
Best Time to Buy and Sell Stock with Cooldown
Solved 
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:

After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
You may only own at most one NeetCoin at a time.
You may complete as many transactions as you like.

Return the maximum profit you can achieve.

Example 1:

Input: prices = [1,3,4,0,4]

Output: 6
Explanation: Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. Total profit is 2 + 4 = 6.

Example 2:

Input: prices = [1]

Output: 0
Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000

## Solution Template
```python
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
                
           
            
```
