class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for start, end, cost in flights:
            graph[start].append([cost, end])
        
        pq = [[0, 0, src]]
        visited = {}
        result = -1

        while pq:
            cost, count, curr = heapq.heappop(pq)

            # If we've reached the destination, return cost
            if curr == dst:
                return cost

            # If we already used up k stops, we can't proceed further
            if count > k:
                continue
            
            
            new_count = count + 1

            for n_cost, neighbor in graph[curr]:
                # if neighbor not in visited:
                heapq.heappush(pq, [n_cost + cost, new_count, neighbor])
        

        return -1

        