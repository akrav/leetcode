class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [temperatures[0]]
        res = []
        for i in range(1, len(temperatures)):

            if stack[-1] >= temperatures[i]:
                stack.append(temperatures[i])
            else:
                count = 1
                while stack != [] and stack[-1] < temperatures[i]:
                    res.append(count)
                    stack.pop()
                    count += 1
                stack.append(temperatures[i])
        return res[::-1]



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_idx = [0]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if stack_idx != []:
                s_idx = stack_idx[-1]
                stack_temp = temperatures[s_idx]

                while stack_idx != [] and temperatures[i] > stack_temp:
                    res[s_idx] = i - s_idx
                    stack_idx.pop()
                    if stack_idx != []:
                        s_idx = stack_idx[-1]
                        stack_temp = temperatures[s_idx]
                
            stack_idx.append(i)

        return res

# _
# 28. 0
# 40. 0
# 35  1
# 36  2
#     1
# 38. 4
#     1

# 6
# 5
# 4. 5-4 =1
# 3  5-3 = 2
#    3-2 = 1
# 1. 5- 1 =4
#    1-0 = 1

        