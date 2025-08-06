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