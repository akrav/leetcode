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