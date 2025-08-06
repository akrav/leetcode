[Back to Table of Contents](../README.md)

# Meeting Rooms II
Difficulty: Medium

## Question
Meeting Rooms II
Solved 
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000

## Solution Template
```python
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

        
```
