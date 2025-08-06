# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         count = 0
#         prev_one = 0
#         prev_two = 1
#         for i in range(0,n):
#             count = prev_one + prev_two

#             prev_one = prev_two
#             prev_two = count
        
#         return count

class Solution:
    def climbStairs(self, n: int) -> int:

        def rec(num):
            if num < 0:
                return 0
            if num == 0:
                return 1
            
            op_one = rec(num-1)
            op_two = rec(num-2)

            return op_one + op_two
        
        return rec(n)
