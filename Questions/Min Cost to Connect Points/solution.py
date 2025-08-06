class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                man_dist = abs(x2-x1) + abs(y2-y1)
                graph[i].append([man_dist, j])
                graph[j].append([man_dist, i])
                

        q = [[0,0]] #cost point
        result = 0
        visited = {}

        while q:
            cost, curr = heapq.heappop(q)
            if curr in visited:
                continue
            
            result += cost

            visited[curr] = True

            for n_cost, neighbor in graph[curr]:
                if neighbor not in visited:
                    heapq.heappush(q, [n_cost, neighbor])
        
        return result
                    