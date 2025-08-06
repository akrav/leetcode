import heapq as hq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_pq = []
        if a != 0:
            hq.heappush(max_pq, (-a, "a"))
        if b != 0:
            hq.heappush(max_pq, (-b, "b"))
        if c != 0:
            hq.heappush(max_pq, (-c, "c"))
        
        res = ""
        while max_pq:
            count, letter = hq.heappop(max_pq)
            if res and len(res) >= 2 and res[-2] == res[-1] == letter and len(max_pq) <= 0:
                return res
            
            if res and len(res) >= 2 and res[-2] == res[-1] == letter:
                count2, letter2 = hq.heappop(max_pq)
                nc = count2 + 1
                res += letter2
                if nc != 0:
                    hq.heappush(max_pq, (nc, letter2))
                hq.heappush(max_pq, (count, letter))
                continue
            
            nc = count + 1
            res += letter
            if nc != 0:
                hq.heappush(max_pq, (nc, letter))

        return res
            

        