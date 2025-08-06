# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

#         graph = defaultdict(list)
#         for a, b, c in times:
#             graph[a].append((b,c))
        
#         visited = {}
        
#         q = [(k, 0)]

#         t = 0 
#         while q:
#             curr, time = heapq.heappop(q)
#             if curr in visited:
#                 continue
#             t = time
#             visited[curr] = True

#             for neighbor, neighbor_time in graph[curr]:
#                 if neighbor not in visited:
#                     heapq.heappush(q, (neighbor, neighbor_time + time))
            
#         print(visited)
#         return t if len(visited) == n else -1


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for a, b, c in times:
            graph[a].append((b, c))

        visited = {}
        
        q = [(0, k)]

        t = 0 
        while q:
            time, curr = heapq.heappop(q)
            if curr in visited:
                continue
            t = time
            visited[curr] = True

            for neighbor, neighbor_time in graph[curr]:
                if neighbor not in visited:
                    heapq.heappush(q, (neighbor_time + time, neighbor))

        print(visited)
        return t if len(visited) == n else -1