[Back to Table of Contents](../../README.md)

# Matchsticks to Square
Difficulty: Medium

## Question
Matchsticks to Square
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108

## Solution Template
```python
# class Solution:
#     def makesquare(self, matchsticks: List[int]) -> bool:
#         #this is a combinations question
#         matchsticks.sort(reverse=True)
#         result = []
#         total_len = sum(matchsticks)

#         if total_len % 2 == 1:
#             return False

#         side_len = total_len/4
#         side_count = 0

#         def rec(start, target_side):
#             nonlocal side_len, side_count

#             if target_side == 0:
#                 side_count += 1
#                 if side_count == 4:
#                     return True
#                 target_side = side_len
            
#             if target_side < 0:
#                 return False
            
            

#             res = False
#             for i in range(start, len(matchsticks)):
#                 val = matchsticks[i]
#                 res = rec(i+1, target_side - val)
        
#             return res
        
#         return rec(0, side_len)




class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #this is a combinations question
        matchsticks.sort(reverse=True)
        result = []
        total_len = sum(matchsticks)

        if total_len % 4 != 0:
            return False

        matchstick_set = [total_len / 4] * 4

        def backtrack(idx):
            #base case
            if idx == len(matchsticks):
                return True
            
            #other choices picking 1 of the 4 sides
            for i in range(4):
                if matchstick_set[i] - matchsticks[idx] >= 0:
                    matchstick_set[i] -= matchsticks[idx]
                    found_a_solution = backtrack(idx+1)
                    if found_a_solution:
                        return True
                    matchstick_set[i] += matchsticks[idx]
            
            return False
        
        return backtrack(0)
```
