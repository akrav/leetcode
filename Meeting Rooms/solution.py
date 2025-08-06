"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        prev = 0
        for curr in range(1, len(intervals)):
            if intervals[prev].end > intervals[curr].start:
                return False
            else:
                prev = curr
        return True