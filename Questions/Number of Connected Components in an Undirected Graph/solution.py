class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = [False] * n

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        

        def bfs(node):
            q = [node]
            visited[node] = True

            while q:
                curr = q.pop(0)

                for neighbor in graph[curr]:
                    if visited[neighbor] == False:
                        visited[neighbor] = True
                        q.append(neighbor)
        
        result = 0
        for i in range(n):
            # if not visited explore tree and mark all nodes as visited
            # if find another node not visited increment the count
            if visited[i] == False:
                result += 1
                bfs(i)
        
        return result