[Back to Table of Contents](../README.md)

# Longest Happy String
Difficulty: Medium

## Question
Longest Happy String
Solved
Medium
Topics
premium lock icon
Companies
Hint
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0

## Solution Template
```python
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
            

        
```
