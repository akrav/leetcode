class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[b].append(a)

        indegree = defaultdict(int)
        for a, b in prerequisites:
            indegree[a] += 1


        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        result = []
        while q:
            curr = q.pop(0)
            result.append(curr)

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(result) < numCourses:
            return []

        return result

        