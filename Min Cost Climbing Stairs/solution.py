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