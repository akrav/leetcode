# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         self.memo = {}
        
#         def rec(n):
#             if n < 0:
#                 return 0
#             if n == 0:
#                 return nums[0]

#             if n in self.memo:
#                 return self.memo[n]
            
#             op_one = rec(n - 1)
#             op_two = rec(n - 2)

#             self.memo[n] = max(op_one, op_two + nums[n])

#             return self.memo[n]
        
#         return rec(len(nums) - 1)



class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        
        prev = nums[0]
        curr = max(nums[0],nums[1])

        print(f"prev: {prev}, curr: {curr}")
        for i in range(2, n):
            count = max(prev + nums[i], curr)
            prev = curr
            curr = count
            print(f"prev: {prev}, curr: {curr}")

        return count