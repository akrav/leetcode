[Back to Table of Contents](../README.md)

# Last Stone Weight
Difficulty: Easy

## Question
Last Stone Weight
Solved 
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:

Input: stones = [2,3,6,2,4]

Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:

Input: stones = [1,2]

Output: 1
Constraints:

1 <= stones.length <= 20
1 <= stones[i] <= 100

## Solution Template
```python
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
```
