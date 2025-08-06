[Back to Table of Contents](../README.md)

# Merge Intervals
Difficulty: Medium

## Question
Merge Intervals
Solved 
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:

Input: intervals = [[1,3],[1,5],[6,7]]

Output: [[1,5],[6,7]]
Example 2:

Input: intervals = [[1,2],[2,3]]

Output: [[1,3]]
Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= start <= end <= 1000

## Solution Template
```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        newInterval = [intervals[0][0],intervals[0][1]]
        for i in range(1, len(intervals)):
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                newInterval = intervals[i]
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        ans.append(newInterval)
        return ans
        
```
