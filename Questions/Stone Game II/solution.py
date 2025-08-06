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