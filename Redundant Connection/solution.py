class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        
        q = []

        for i in range(n+1):
            if indegree[i] == 1:
                q.append(i)
        

        while q:
            curr = q.pop()
            indegree[curr] -= 1
            for neighbor in graph[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 1:
                    q.append(neighbor)

        for a, b in reversed(edges):
            if indegree[a] == 2 and indegree[b] == 2:
                return [a, b]

        return []
        