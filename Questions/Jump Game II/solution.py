class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        graph = defaultdict(list)

        for i in range(len(nums)):
            for j in range(1, nums[i]+1):
                graph[i].append(i + j)
        
        print(graph)
        
        queue = [0]
        jumps = 0
        

        while queue:
            jumps += 1
            level_size = len(queue)
            for i in range(level_size):
                curr = queue.pop(0)

                for neighbors in graph[curr]:
                    if neighbors >= len(nums)-1:
                        return jumps
                    queue.append(neighbors)
        
        return 0