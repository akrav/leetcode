[Back to Table of Contents](../../README.md)

# Stone Game
Difficulty: Medium

## Question
Stone Game
Solved
Medium
Topics
premium lock icon
Companies
Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.

Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.

 

Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alice starts first, and can only take the first 5 or the last 5.
Say she takes the first 5, so that the row becomes [3, 4, 5].
If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
Example 2:

Input: piles = [3,7,2,3]
Output: true
 

Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles[i]) is odd.

## Solution Template
```python
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         if len(piles) == 1:
#             return True
        
#         sum_piles = sum(piles)
#         win_num = sum_piles // 2

#         visited = {}

#         def rec(updated_piles, alices_score, alices_turn):
#             if len(updated_piles) == 0:
#                 return alices_score
            
#             if f"({updated_piles}, {alices_score})" in visited.keys():
#                 return visited[f"({updated_piles}, {alices_score})"]

#             left_pile = updated_piles[0]
#             after_left_removed = updated_piles[1:]

#             right_pile = updated_piles[-1]
#             after_right_removed = updated_piles[:-1]

#             if alices_turn:
#                 l_alices_score = alices_score + left_pile
#                 lr = rec(after_left_removed, l_alices_score, not alices_turn)

#                 r_alices_score = alices_score + right_pile
#                 rr = rec(after_right_removed, r_alices_score, not alices_turn)

#                 score = max(lr, rr)
            
#             else:
#                 lr = rec(after_left_removed, alices_score, not alices_turn)

#                 rr = rec(after_right_removed, alices_score, not alices_turn)

#                 score = min(lr, rr)

#                 visited[f"({updated_piles}, {alices_score})"] = score
            
#             return score
        

#         return rec(piles, 0, True) > win_num


# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         n = len(piles)
#         memo = {}
        
#         def rec(l, r, alice_turn):
#             if l > r:
#                 return 0
            
#             if (l, r, alice_turn) in memo:
#                 return memo[(l, r, alice_turn)]
            
#             if alice_turn:
#                 # Alice adds to her score
#                 score_left = piles[l] + rec(l+1, r, False)
#                 score_right = piles[r] + rec(l, r-1, False)
#                 best_score = max(score_left, score_right)
#             else:
#                 # Bob's turn; if you want to maximize Alice's final score, 
#                 # you can interpret Bob's turn as "Bob subtracts from Alice's net"
#                 # Or interpret Bob as playing optimally and we want Alice's net.
#                 # Typically we'd do:
#                 score_left = rec(l+1, r, True) - piles[l]
#                 score_right = rec(l, r-1, True) - piles[r]
#                 best_score = min(score_left, score_right)
            
#             memo[(l, r, alice_turn)] = best_score
#             return best_score
        
#         total = sum(piles)
#         # bestScore is the difference between Alice's and Bob's score if we interpret 
#         # Bob subtracting from the net. If bestScore > 0, Alice has more stones.
#         bestScore = rec(0, n-1, True)
#         return bestScore > 0


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = {}
        def rec(left, right, difference, alices_turn):
            if left > right:
                return difference
            
            if (left, right, alices_turn) in memo:
                return memo[(left, right, alices_turn)]
            
            option1 = piles[left]
            option2 = piles[right]

            if not alices_turn:
                option1 *= -1
                option2 *= -1
            
            play1 = rec(left + 1, right, difference + option1, not alices_turn)
            play2 = rec(left, right - 1, difference + option2, not alices_turn)

            memo[(left, right, alices_turn)] = max(play1, play2)

            return memo[(left, right, alices_turn)]
        
        return rec(0, n-1, 0, True) > 0
```
