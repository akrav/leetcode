class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        indegree = defaultdict(int)

        for i in range(numCourses):
            indegree[i] = 0


        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        
        # q = []
        # for i in range(numCourses):
        #     if indegree[i] == 0:
        #         q.append()
        
        res = []
        for question_prereq, target in queries:
            q = []
            q.append(question_prereq)
            query_solved = False
            visited = {}
            while q:
                curr_course = q.pop(0)
                if curr_course not in visited:
                    visited[curr_course] = True
                    for neighbor in adj[curr_course]:
                        if neighbor == target:
                            query_solved = True
                            break
                        q.append(neighbor)
                    if query_solved:
                        break
            res.append(query_solved)
        return res