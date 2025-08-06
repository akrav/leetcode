[Back to Table of Contents](../../README.md)

# Reorganize String
Difficulty: Medium

## Question
Reorganize String
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

## Solution Template
```python
# import heapq as hq
# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         pq = []

#         dic_count = defaultdict(int)
#         for letter in s:
#             dic_count[letter] += 1

#         if max(dic_count.values()) > sum(dic_count.values()) - max(dic_count.values()) +1:
#             return ""
        

#         dic_count = dict(sorted(dic_count.items(), key=lambda item: item[1], reverse=True))
#         # print(f"dict_count")

#         res = ""
#         while sum(dic_count.values()) > 0:
#             for new_letter in dic_count.keys():
#                 if res and new_letter == res[-1]:
#                     continue
#                 if dic_count[new_letter] <= 0:
#                     continue
#                 res += new_letter
#                 dic_count[new_letter] -= 1
#                 break
        
#         return res






import heapq as hq
class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = []

        dic_count = defaultdict(int)
        for letter in s:
            dic_count[letter] += 1

        if max(dic_count.values()) > sum(dic_count.values()) - max(dic_count.values()) +1:
            return ""

        for key, value in dic_count.items():
            hq.heappush(pq, (-value, key))
        
        res = ''
        while pq:
            count, letter = hq.heappop(pq)
            if res and res[-1] == letter:
                count_2, letter_2 = hq.heappop(pq)
                res += letter_2
                nc = count_2+1
                if nc != 0:
                    hq.heappush(pq, (nc, letter_2))
                hq.heappush(pq, (count, letter))
                continue
            
            res += letter
            nc = count+1
            if nc != 0:
                hq.heappush(pq, (nc, letter))

        
        return res

# class Solution:
#     def reorganizeString(self, s: str) -> str:
#         count = Counter(s)
#         maxHeap = [[-cnt, char] for char, cnt in count.items()]
#         heapq.heapify(maxHeap)
        
#         prev = None
#         res = ""
#         while maxHeap or prev:
#             if prev and not maxHeap:
#                 return ""
            
#             cnt, char = heapq.heappop(maxHeap)
#             res += char
#             cnt += 1

#             if prev:
#                 heapq.heappush(maxHeap, prev)
#                 prev = None
            
#             if cnt != 0:
#                 prev = [cnt, char]
        
#         return res
```
