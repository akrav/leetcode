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