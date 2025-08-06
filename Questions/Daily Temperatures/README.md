[Back to Table of Contents](../../README.md)

# Daily Temperatures
Difficulty: Medium

## Question
Daily Temperatures
Solved 
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]
Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]
Constraints:

1 <= temperatures.length <= 1000.
1 <= temperatures[i] <= 100

## Solution Template
```python
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

        
```
