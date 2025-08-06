[Back to Table of Contents](../README.md)

# Number of Connected Components in an Undirected Graph
Difficulty: Medium

## Question
Number of Connected Components in an Undirected Graph
Solved 
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2

## Solution Template
```python
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
```
