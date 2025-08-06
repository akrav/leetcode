[Back to Table of Contents](../README.md)

# Task Scheduler
Difficulty: Medium

## Question
Task Scheduler
Solved 
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2

Output: 5
Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3

Output: 9
Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

Constraints:

1 <= tasks.length <= 1000
0 <= n <= 100

## Solution Template
```python
import heapq as hq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = []
        h = []

        time = 0

        dic = defaultdict(int)
        for task in tasks:
            dic[task] += 1
        
        count = list(dic.values())
        count.sort(reverse=True)

        for c in count:
            hq.heappush(h, (-c, time))
        
        
        while h != [] or queue != []:
            # print(f"start: h: {h}, queue: {queue}")
            if h != []:
                task_remaining, time_task_should_finish = hq.heappop(h)

                if time >= time_task_should_finish:
                    new_task_remaining = task_remaining+1
                    if new_task_remaining < 0:

                        queue.append((new_task_remaining, time+n+1))
            
            

            time += 1
            if queue != [] and queue[0][1] == time:
                hq.heappush(h, queue.pop(0))
            # print(f"end: h: {h}, queue: {queue}")
        
        return time
```
