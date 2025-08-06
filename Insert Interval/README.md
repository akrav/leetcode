[Back to Table of Contents](../README.md)

# Insert Interval
Difficulty: Medium

## Question
Insert Interval
Solved 
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. intervals is initially sorted in ascending order by start_i.

You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

Example 1:

Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

Output: [[1,6]]
Example 2:

Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

Output: [[1,2],[3,5],[6,7],[9,10]]
Constraints:

0 <= intervals.length <= 1000
newInterval.length == intervals[i].length == 2
0 <= start <= end <= 1000

## Solution Template
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # first_start = intervals[0][0]
        # first_end = intervals[0][1]

        # for i in range(1, len(intervals)):
        #     second_start = intervals[i][0]
        #     second_end = intervals[i][1]

        #     if newInterval[0] > first_end and newInterval[1] < second_start:
        #         #insert interval into i postion and return
        #         print(f"here if 1")
        #         intervals.insert(i, newInterval)
        #         return intervals
        #     elif newInterval[0] <= first_end and newInterval[1] >= second_start:
        #         print(f"here if 2")
        #         new_list = [min(newInterval[0], first_start), max(newInterval[1], second_end)]
        #         intervals.pop(i)
        #         intervals.insert(i, new_list)
        #         intervals.pop(i-1)
        #     elif newInterval[0] <= first_end and newInterval[1] < second_start:
        #         print(f"here if 3eee")
        #         intervals[i-1][1] = max(first_end, newInterval[1])

        #     elif newInterval[0] >= first_end and newInterval[1] <= second_end:
        #         print(f"here if 3")
        #         new_list = [min(newInterval[0], first_end), max(newInterval[1], second_end)]
        #         intervals.pop(i)
        #         intervals.insert(i, new_list)
            
        #     elif newInterval[0] <= first_start and newInterval[1] <= first_end:
        #         print(f"here if 4")
        #         new_list = [min(newInterval[0], first_start), max(newInterval[1], first_end)]
        #         intervals.pop(i-1)
        #         intervals.insert(i-1, new_list)

        #     start = second_start
        #     end = second_end
        
        # print(intervals)
        # return intervals
        ans = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                ans.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        ans.append(newInterval)
        return ans
```
