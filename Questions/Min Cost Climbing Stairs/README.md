[Back to Table of Contents](../../README.md)

# Min Cost Climbing Stairs
Difficulty: Easy

## Question
Min Cost Climbing Stairs
Solved 
You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.

Example 1:

Input: cost = [1,2,3]

Output: 2
Explanation: We can start at index = 1 and pay the cost of cost[1] = 2 and take two steps to reach the top. The total cost is 2.

Example 2:

Input: cost = [1,2,1,2,1,1,1]

Output: 4
Explanation: Start at index = 0.

Pay the cost of cost[0] = 1 and take two steps to reach index = 2.
Pay the cost of cost[2] = 1 and take two steps to reach index = 4.
Pay the cost of cost[4] = 1 and take two steps to reach index = 6.
Pay the cost of cost[6] = 1 and take one step to reach the top.
The total cost is 4.
Constraints:

2 <= cost.length <= 100
0 <= cost[i] <= 100

## Solution Template
```python
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         def rec(n):
#             if n < 0:
#                 return 0
#             if n == 0:
#                 return cost[n]
            
#             op_one = rec(n - 1)
#             op_two = rec(n - 2)

#             if n == len(cost):
#                 return min(op_one, op_two)

#             return min(op_one, op_two) + cost[n]
        
#         return rec(len(cost))


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        prev = cost[0]
        curr = cost[1]
        count = 0
        for i in range(2,len(cost)):
            count = min(prev, curr) + cost[i]


            prev = curr
            curr = count
        
        return min(prev, curr)
```
