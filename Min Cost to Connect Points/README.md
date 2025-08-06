[Back to Table of Contents](../README.md)

# Min Cost to Connect Points
Difficulty: Medium

## Question
Min Cost to Connect Points
Solved 
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

Example 1:



Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

Output: 10
Constraints:

1 <= points.length <= 1000
-1000 <= xi, yi <= 1000

## Solution Template
```python
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
                    
```
