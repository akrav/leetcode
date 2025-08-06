# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         res = []
#         for i in range(len(nums)-k+1):
#             res.append(max(nums[i:i+k]))
#         return res

import heapq as hq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []
        res = []
        for i in range(len(nums)):
            hq.heappush(pq, (-1 * nums[i], i))
            if i >= k - 1:
                while pq[0][1] <= i - k: # while idx of the largest value in the window 
                                         # is leq to the idx of the element being removed
                                         # from the window we remove it
                    hq.heappop(pq)       
                res.append(-1*pq[0][0])
        return res
                