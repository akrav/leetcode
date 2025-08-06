class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        indegree = defaultdict(int)
        for a, b in prerequisites:
            indegree[b] += 1
        
        q = []
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        result = []
        while q:
            level_size = len(q)
            curr = q.pop()
            result.append(curr)

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(result) < numCourses:
            return False
        return True
        