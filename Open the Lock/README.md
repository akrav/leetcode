[Back to Table of Contents](../README.md)

# Open the Lock
Difficulty: Medium

## Question
Open the Lock
Solved
Medium
Topics
premium lock icon
Companies
Hint
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
 

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.

## Solution Template
```python
# class Solution:
#     def openLock(self, deadends: List[str], target: str) -> int:

#         def generate_possible_moves(code, seen):
#             ans = []
#             for i in range(len(code)):
#                 if code[i] == "0":
#                     option_1 = code[:i] + "1" + code[i+1:]
#                     option_2 = code[:i] + "9" + code[i+1:]
#                     if option_1 not in deadends and seen[option_1] == False:
#                         ans.append(option_1)
#                     if option_2 not in deadends and seen[option_2] == False:
#                         ans.append(option_2)
#                     continue
#                 if code[i] == "9":
#                     option_1 = code[:i] + "0" + code[i+1:]
#                     option_2 = code[:i] + "8" + code[i+1:]
#                     if option_1 not in deadends and seen[option_1] == False:
#                         ans.append(option_1)
#                     if option_2 not in deadends and seen[option_2] == False:
#                         ans.append(option_2)
#                     continue
#                 num = int(code[i])

#                 option_1 = code[:i] + str(num+1) + code[i+1:]
#                 option_2 = code[:i] + str(num-1) + code[i+1:]
#                 if option_1 not in deadends and seen[option_1] == False:
#                     ans.append(option_1)
#                 if option_2 not in deadends and seen[option_2] == False:
#                     ans.append(option_2)

#             return ans
        
        
#         def bfs(code, target, seen):
#             q = [code]
#             depth = 0
#             while q:
#                 len_q = len(q)
#                 for i in range(len_q):
#                     curr_code = q.pop(0)
#                     if seen[curr_code] == False:
#                         seen[curr_code] = True
#                         q += generate_possible_moves(curr_code, seen)

#                         if curr_code == target:
#                             return depth
                
#                 depth += 1
            
#             return -1

#         seen = defaultdict(lambda: False)
#         return bfs("0000", target, seen) if "0000" not in deadends else -1


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        
        def bfs(code, target, seen):
            q = [code]
            depth = 0
            while q:
                len_q = len(q)
                for i in range(len_q):
                    curr_code = q.pop(0)
                    if seen[curr_code] == False:
                        seen[curr_code] = True
                        q += children(curr_code)

                        if curr_code == target:
                            return depth
                depth += 1
            
            return -1

        seen = defaultdict(lambda: False)
        for deadend in deadends:
            seen[deadend] = True
        return bfs("0000", target, seen) if "0000" not in deadends else -1
```
