import heapq as hq 

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.pq = []
        for num in nums:
            hq.heappush(self.pq, num)
        
        while len(self.pq) > self.k:
            hq.heappop(self.pq)
        

    def add(self, val: int) -> int:
        hq.heappush(self.pq, val)
        if len(self.pq) > self.k:
            hq.heappop(self.pq)
        return self.pq[0]