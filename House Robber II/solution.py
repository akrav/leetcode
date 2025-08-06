# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         t = len(nums)
#         if t == 1:
#             return nums[0]
#         if t == 2:
#             return max(nums[0], nums[1])

#         self.memo = {}


#         def rec(start, end):
#             if end < start:
#                 return 0
#             if end == start:
#                 return nums[start]
#             if end in self.memo:
#                 return self.memo[end]
            
#             op_one = rec(start, end - 1)
#             op_two = rec(start, end - 2)

#             self.memo[end] = max(op_two + nums[end], op_one)

#             return self.memo[end]
        
#         one = rec(0, t-2)
#         self.memo = {}
#         two = rec(1, t-1)
        
#         return max(one, two)


class Solution:
    def rob(self, nums: List[int]) -> int:
        t = len(nums)
        if t == 1:
            return nums[0]
        if t == 2:
            return max(nums[0], nums[1])
            
        prev_one = nums[0]
        curr_one = max(nums[0], nums[1])
        count_one = 0

        for i in range(2,t-1):
            count_one = max(prev_one + nums[i], curr_one)
            prev_one = curr_one
            curr_one = count_one
        
        ans_one = max(curr_one, prev_one)

        prev_two = nums[1]
        curr_two = max(nums[2], nums[1])
        count_two = 0
        for i in range(3, t):
            count_two = max(prev_two + nums[i], curr_two)
            prev_two = curr_two
            curr_two = count_two
        
        ans_two = max(curr_two, prev_two)

        return max(ans_one, ans_two)