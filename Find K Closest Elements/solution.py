# import heapq as hq
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         pq = []


#         for i in range(len(arr)):
#             if len(pq) < k:
#                 hq.heappush(pq, (-1 * abs(x - arr[i]),arr[i]))
#             else:
#                 difference, val = pq[0]
#                 if difference < (-1 * abs(x - arr[i])):
#                     hq.heappop(pq)
#                     hq.heappush(pq, (-1 * abs(x - arr[i]),arr[i]))
#         res = []
#         while pq:
#             res.append(hq.heappop(pq)[1])
#         res.sort()
#         return res

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        
        return arr[l: r + 1]