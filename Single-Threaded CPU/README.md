[Back to Table of Contents](../README.md)

# Single-Threaded CPU
Difficulty: Medium

## Question
Single-Threaded CPU
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

 

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
Example 2:

Input: tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
Output: [4,3,2,0,1]
Explanation: The events go as follows:
- At time = 7, all the tasks become available. Available tasks = {0,1,2,3,4}.
- Also at time = 7, the idle CPU starts processing task 4. Available tasks = {0,1,2,3}.
- At time = 9, the CPU finishes task 4 and starts processing task 3. Available tasks = {0,1,2}.
- At time = 13, the CPU finishes task 3 and starts processing task 2. Available tasks = {0,1}.
- At time = 18, the CPU finishes task 2 and starts processing task 0. Available tasks = {1}.
- At time = 28, the CPU finishes task 0 and starts processing task 1. Available tasks = {}.
- At time = 40, the CPU finishes task 1 and becomes idle.
 

Constraints:

tasks.length == n
1 <= n <= 105
1 <= enqueueTimei, processingTimei <= 109

## Solution Template
```python
import heapq as hq

# class Solution:
#     def getOrder(self, tasks: List[List[int]]) -> List[int]:
#         #(time_done, time_added, idx)
#         pq = []
#         for idx in range(len(tasks)):
#             hq.heappush(pq, (tasks[idx][0] + tasks[idx][1], tasks[idx][0], idx))
        
#         res = []
#         for i in range(len(pq)):
#             end_time, start_time, idx = hq.heappop(pq)
#             res.append(idx)
        
#         return res

# class Solution:
#     def getOrder(self, tasks: List[List[int]]) -> List[int]:
#         #(time_done, time_added, idx)
#         available_tasks = []
#         processing_task = []
#         res = []
#         graph = defaultdict(list)
#         max_time = 0
#         for i in range(len(tasks)):
#             max_time = max(max_time, tasks[i][1] + tasks[i][0])
#             graph[tasks[i][0]].append((tasks[i][1], i))
        

#         process_task_time = 0
#         for time in range(max_time+1):
#             if graph[time] != []:
#                 for processing_time, idx in graph[time]:
#                     hq.heappush(available_tasks, (processing_time, idx))
            
#             if processing_task and process_task_time <= 0:
#                 processing_time, idx = hq.heappop(processing_task)
#                 res.append(idx)
            
#             if processing_task == [] and available_tasks != []:
#                 next_task = hq.heappop(available_tasks)
#                 process_task_time = next_task[0]
#                 hq.heappush(processing_task, next_task)
            
#             process_task_time -= 1

#         if processing_task != []:
#             res.append(hq.heappop(processing_task)[1])
#         for i in range(len(available_tasks)):
#             processing_time, idx = hq.heappop(available_tasks)
#             res.append(idx)

#         return res


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])

        res, minHeap = [], []
        i, time = 0, tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not minHeap:
                time = tasks[i][0]
            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
        return res

# [
#     [19,13],  32, 19, 0
#     [16,9],   25, 16, 1
#     [21,10],  31, 21, 2
#     [32,25],  57, 32, 3
#     [37,4],   41, 37, 4
#     [49,24],  73, 49, 5
#     [2,15],   17, 2, 6
#     [38,41],  79, 38, 7
#     [37,34],  71, 37, 8
#     [33,6],   39, 33, 9
#     [45,4],   49, 45, 10
#     [18,18],  36, 18, 11
#     [46,39],  85, 46, 12
#     [12,24]]  36, 12, 13

#     17, 2, 6
#     25, 16, 1
#     31, 21, 2
#     39, 33, 9
#     41, 37, 4
#     49, 45, 10
#     32, 19, 0
#     36, 18, 11
#     73, 49, 5
#     36, 12, 13
#     57, 32, 3
#     71, 37, 8
#     85, 46, 12
#     79, 38, 7
    
```
