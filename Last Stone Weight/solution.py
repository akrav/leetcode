import heapq as hq
# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         if len(stones) == 0:
#             return 0
#         elif len(stones) == 1:
#             return stones[0]
#         hq._heapify_max(stones)
#         pq = stones
#         print(f"pq: {pq}")

#         while len(pq) > 1:
#             x = hq._heappop_max(pq)
#             y = hq._heappop_max(pq)

#             print(f"x: {x}, y: {y}")

#             val = abs(y-x)
#             if val == 0:
#                 continue
#             hq.heappush(pq, val)
#             hq._heapify_max(pq) 
#         return pq[0] if len(pq) > 0 else 0
            
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])