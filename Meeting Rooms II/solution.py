"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]
        start.sort()
        end.sort()

        count = 0
        max_at_the_same_time = 0

        start_pointer = 0
        end_pointer = 0

        while start_pointer < len(intervals):
            if start[start_pointer] < end[end_pointer]:
                count += 1
                start_pointer += 1
            else: 
                end_pointer += 1
                count -= 1
            
            max_at_the_same_time = max(max_at_the_same_time, count)

        return max_at_the_same_time

        