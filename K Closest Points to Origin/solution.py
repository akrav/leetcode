import heapq as hq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidian_distance(point_1):
            return ((point_1[0] - 0)**2 + (point_1[1] - 0)**2)**(1/2)
        
        pq = []

        for point in points:
            hq.heappush(pq, (euclidian_distance(point), point))
        
        ans = []
        for i in range(k):
            dis, point = hq.heappop(pq)
            ans.append(point)
        return ans