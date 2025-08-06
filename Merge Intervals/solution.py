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
        