class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # to be a tree there are n nodes and n-1 edges
        if len(edges) != n - 1:
            return False
        
        if n == 1 and len(edges) == 0:
            return True

        graph = defaultdict(list)
        indegree = defaultdict(int)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for a, b in edges:
            indegree[a] += 1
            indegree[b] += 1
        
        q = []
        for i in range(n):
            # to be a undirected graph the lowest indegree is 1 not 0 for directed, 
            # if we see 0 there is a problem if there are more than 1 nodes in the tree
            if indegree[i] == 1:
                q.append(i)
            elif indegree[i] == 0 and n>1:
                return False

        result = []
        while q:
            curr = q.pop(0)
            result.append(curr)
            indegree[curr] -= 1

            for neighbor in graph[curr]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 1:
                    q.append(neighbor)
        
        if len(result) < n:
            return False
        
        return True
        