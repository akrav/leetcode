# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         intervals.sort()
#         new_interval = intervals[0][:]
#         count = 0

#         for i in range(1, len(intervals)):
#             if new_interval[1] <= intervals[i][0]:
#                 new_interval = intervals[i]
#                 continue
#             elif new_interval[0] >= intervals[i][1]:
#                 continue
#             else:
#                 new_interval = [min(new_interval[0], intervals[i][0]), min(new_interval[1], intervals[i][1])]
#                 count += 1
        
#         return count

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        count = 0

        for start, end in intervals[1:]:
            if prev_end <= start:
                prev_end = end
            else:
                prev_end = min(prev_end, end)
                count += 1
        
        return count