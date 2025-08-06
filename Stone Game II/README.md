[Back to Table of Contents](../README.md)

# Stone Game II
Difficulty: Medium

## Question
Stone Game II
Solved
Medium
Topics
premium lock icon
Companies
Hint
Alice and Bob continue their games with piles of stones. There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

 

Example 1:

Input: piles = [2,7,9,4,4]

Output: 10

Explanation:

If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.
If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 stones in total.
So we return 10 since it's larger.

Example 2:

Input: piles = [1,2,3,4,5,100]

Output: 104

 

Constraints:

1 <= piles.length <= 100
1 <= piles[i] <= 104

## Solution Template
```python
# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
#         n = len(piles)
#         memo = {}

#         def rec(left, right, alices_turn, M):
#             nonlocal n
#             if left > right:
#                 return 0
#             if (left, right, alices_turn, M) in memo:
#                 return memo[(left, right, alices_turn, M)]
            
#             remaining = right - left + 1
#             pile_count_left = 0
#             if alices_turn:
#                 best = 0
#                 for i in range(min(2 * M, remaining) + 1):
#                     i = i + 1
#                     current = sum(piles[left:left + i]) + rec(left + i, right, False, max(M, i))
#                     best = max(best, current)
                
#                 memo[(left, right, alices_turn, M)] = best
#                 return memo[(left, right, alices_turn, M)]

#             else:
#                 worst = 100000000
#                 for i in range(min(2 * M, remaining) + 1):
#                     i = i + 1

#                     current = rec(left + i, right, True, max(M, i))

#                     worst = min(worst, current)
                
#                 memo[(left, right, alices_turn, M)] = worst
#                 return memo[(left, right, alices_turn, M)]

        
#         return rec(0, n-1, True, 1)

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}

        def rec(left, right, alices_turn, M):
            nonlocal n
            if left > right:
                return 0
            if (left, right, alices_turn, M) in memo:
                return memo[(left, right, alices_turn, M)]
            
            remaining = right - left + 1
            pile_count_left = 0
            if alices_turn:
                best = 0
                for i in range(min(2 * M, remaining)):
                    i = i + 1
                    current = sum(piles[left:left + i]) + rec(left + i, right, False, max(M, i))
                    best = max(best, current)
                
                memo[(left, right, alices_turn, M)] = best
                return memo[(left, right, alices_turn, M)]

            else:
                worst = 100000000
                for i in range(min(2 * M, remaining)):
                    i = i + 1

                    current = rec(left + i, right, True, max(M, i))

                    worst = min(worst, current)
                
                memo[(left, right, alices_turn, M)] = worst
                return memo[(left, right, alices_turn, M)]

        
        return rec(0, n-1, True, 1)


# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:
#         n = len(piles)
#         memo = {}

#         def rec(left, right, alices_turn, M):
#             nonlocal n
#             if left > right:
#                 return 0
#             if (left, right, alices_turn, M) in memo:
#                 return memo[(left, right, alices_turn, M)]
            
#             remaining = right - left + 1
#             if alices_turn:
#                 best = 0
#                 # x goes from 1 to the allowed maximum number of piles.
#                 for x in range(1, min(2 * M, remaining) + 1):
#                     current = sum(piles[left:left + x]) + rec(left + x, right, False, max(M, x))
#                     best = max(best, current)
#                 memo[(left, right, alices_turn, M)] = best
#                 return best
#             else:
#                 worst = float('inf')
#                 for x in range(1, min(2 * M, remaining) + 1):
#                     current = rec(left + x, right, True, max(M, x))
#                     worst = min(worst, current)
#                 memo[(left, right, alices_turn, M)] = worst
#                 return worst

#         return rec(0, n - 1, True, 1)
```
