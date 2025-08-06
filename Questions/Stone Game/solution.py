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