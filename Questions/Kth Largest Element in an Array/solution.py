import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        hq.heapify(nums)
        pq = nums

        while len(pq) > k:
            hq.heappop(pq)
        
        return hq.heappop(pq)