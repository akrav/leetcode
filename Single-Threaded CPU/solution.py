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
    