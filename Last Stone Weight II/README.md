[Back to Table of Contents](../README.md)

# Last Stone Weight II
Difficulty: Medium

## Question
Last Stone Weight II
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], then that's the optimal value.
Example 2:

Input: stones = [31,26,33,21,40]
Output: 5
 

Constraints:

1 <= stones.length <= 30
1 <= stones[i] <= 100

## Solution Template
```python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = (stone_sum + 1)//2
        memo = {}


        #the goal is to get 0, so if the sum is 38 we are looking for stones adding to 19
        # if the sum is 39 we will have at best value of 1 left since 19 will cancel with 19 stones leaving 1
        # so we really have a target of 19 that if we reach -1 we found out answer
    
        def rec(i, val):
            print(f"val <= 0: {val <= 0}, i == len(stones): {i == len(stones)}")
            if val <= 0 or i == len(stones):
                pile1 = stone_sum - target - abs(val)
                pile2 = target + abs(val)
                print(f"stone_sum: {stone_sum}, target: {target}, val: {val}, pile1: {pile1}, pile2: {pile2}")

                return pile2 - pile1
            if (i, val) in memo:
                return memo[(i,val)]
            
            memo[(i,val)] = min(rec(i + 1, val), rec(i + 1, val - stones[i]))
            return memo[(i,val)]
        
        return rec(0, target)
```
