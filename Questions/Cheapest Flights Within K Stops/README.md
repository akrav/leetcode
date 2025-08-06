[Back to Table of Contents](../../README.md)

# Cheapest Flights Within K Stops
Difficulty: Medium

## Question
Cheapest Flights Within K Stops
Solved 
There are n airports, labeled from 0 to n - 1, which are connected by some flights. You are given an array flights where flights[i] = [from_i, to_i, price_i] represents a one-way flight from airport from_i to airport to_i with cost price_i. You may assume there are no duplicate flights and no flights from an airport to itself.

You are also given three integers src, dst, and k where:

src is the starting airport
dst is the destination airport
src != dst
k is the maximum number of stops you can make (not including src and dst)
Return the cheapest price from src to dst with at most k stops, or return -1 if it is impossible.

Example 1:



Input: n = 4, flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]], src = 0, dst = 3, k = 1

Output: 500
Explanation:
The optimal path with at most 1 stop from airport 0 to 3 is shown in red, with total cost 200 + 300 = 500.
Note that the path [0 -> 1 -> 2 -> 3] costs only 400, and thus is cheaper, but it requires 2 stops, which is more than k.

Example 2:



Input: n = 3, flights = [[1,0,100],[1,2,200],[0,2,100]], src = 1, dst = 2, k = 1

Output: 200
Explanation:
The optimal path with at most 1 stop from airport 1 to 2 is shown in red and has cost 200.

Constraints:

1 <= n <= 100
fromi != toi
1 <= pricei <= 1000
0 <= src, dst, k < n

## Solution Template
```python
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

        
```
