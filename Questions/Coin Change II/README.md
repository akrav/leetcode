[Back to Table of Contents](../../README.md)

# Coin Change II
Difficulty: Medium

## Question
Coin Change II
Solved 
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.

Example 1:

Input: amount = 4, coins = [1,2,3]

Output: 4
Explanation:

1+1+1+1 = 4
1+1+2 = 4
2+2 = 4
1+3 = 4
Example 2:

Input: amount = 7, coins = [2,4]

Output: 0
Constraints:

1 <= coins.length <= 100
1 <= coins[i] <= 5000
0 <= amount <= 5000

## Solution Template
```python
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
        
```
