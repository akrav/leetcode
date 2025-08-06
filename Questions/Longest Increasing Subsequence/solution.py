# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         self.res = []

#         def rec(idx, path):
#             if idx == len(nums):
#                 self.res.append(path[:])
#                 return

#             if path == []:
#                 path.append(nums[idx])
#                 rec(idx + 1, path)
#                 path.pop()
#                 rec(idx + 1, path)
#             else:
#                 last_taken = path[-1]

#                 if nums[idx] > last_taken:
#                     path.append(nums[idx])
#                     rec(idx + 1, path)
#                     path.pop()
#                 rec(idx + 1, path)
            
#             return
#         rec(0, [])
#         max_length = 0

#         for ans in self.res:
#             max_length = max(max_length, len(ans))

#         return max_length


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        self.res = []

        def rec(idx, last_taken_idx):
            if idx == len(nums):
                return 0
            taken = 0
            not_taken = 0
            if last_taken_idx == -1:
                taken = rec(idx + 1, idx) + 1
                not_taken = rec(idx + 1, last_taken_idx)
            else:
                if nums[idx] > nums[last_taken_idx]:
                    taken = rec(idx + 1, idx) + 1
                not_taken = rec(idx + 1, last_taken_idx)
            
            return max(taken, not_taken)
        

        return rec(0, -1)